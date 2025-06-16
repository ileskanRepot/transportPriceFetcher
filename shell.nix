{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.requests  # add more as needed
    pkgs.python3Packages.psycopg2  # add more as needed
  ];
}
