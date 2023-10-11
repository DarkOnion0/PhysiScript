{
  description = "A small set of python scripts to help physic students";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

    flake-parts.url = "github:hercules-ci/flake-parts";

    devenv.url = "github:cachix/devenv";
  };

  outputs = inputs @ {
    self,
    nixpkgs,
    flake-parts,
    devenv,
    ...
  }:
    flake-parts.lib.mkFlake {inherit inputs;} {
      debug = true;
      systems = ["x86_64-linux" "aarch64-linux"];
      perSystem = {
        config,
        self',
        inputs',
        pkgs,
        system,
        lib,
        ...
      }: let
        prodPackages = with pkgs; [
          (python3.withPackages (ps:
            with ps; [
              jupyter
              numpy
              matplotlib
              scipy
            ]))

          pandoc
          pandoc-include
        ];
      in {
        devShells = {
          default = devenv.lib.mkShell {
            inherit inputs pkgs;
            modules = [
              {
                packages = with pkgs;
                  [
                    # Python
                    black
                    nodePackages.pyright

                    # Nix
                    alejandra
                    nil
                  ]
                  ++ prodPackages;
                scripts = {
                  start.exec = "jupyter notebook --no-browser";
                };

                pre-commit.hooks = {
                  alejandra.enable = true;
                  black.enable = true;
                  prettier.enable = true;
                };
              }
            ];
          };
        };
        packages = rec {
          default = notebooks;

          notebooks = pkgs.stdenv.mkDerivation {
            name = "notebooks";
            version = "0.1.0";
            src = ./.;

            dontUnpack = true;

            buildInputs = prodPackages;

            buildPhase = ''
                mkdir -p $out/generated/

                cd $src

                ls -larth . src/ src/generic/

                file -i src/generic/main.py

                for subfolders in generic regression titration; do
                  pandoc --filter pandoc-include -i src/main.md src/$subfolders/main.md -o $out\/generated/$subfolders.ipynb
              done
            '';
          };
        };
      };
    };
}
