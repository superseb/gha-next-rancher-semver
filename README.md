# Next Rancher semver

This action prints the next semantic version based on current tags and given parameters.

Current version has some Rancher quirks as the versioning is not real semantic.

## Inputs

## `prefix`

**Required** The prefix to use when filtering existing tags

## `bump`

**Required** What part of the version to bump (prerelease, minor, major)

## Outputs

## `version`

The generated semantic version

## Example usage

```
uses: actions/next-rancher-semver@v1
with:
  prefix: 'v2.6.4'
  bump: 'prerelease'
```
