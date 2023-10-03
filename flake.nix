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
        pythonPackages = ps:
          with ps; [
            jupyter
            numpy
            matplotlib
            scipy
          ];
      in {
        devShells = {
          default = devenv.lib.mkShell {
            inherit inputs pkgs;
            modules = [
              {
                packages = with pkgs; [
                  # Python
                  (python3.withPackages pythonPackages)
                  black

                  # Formatting
                  pandoc

                  # Nix
                  alejandra
                  nil
                ];
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
      };
    };
}
