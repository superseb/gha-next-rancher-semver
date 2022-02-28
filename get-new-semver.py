#!/usr/bin/env python3
from github import Github
import semver, getopt, sys, os

def main(argv):
    required_env_vars = [ "GITHUB_TOKEN", "GITHUB_REPOSITORY" ]
    for env_var in required_env_vars:
        if env_var not in os.environ:
            raise EnvironmentError("{} is not set".format(env_var))

    token = os.getenv('GITHUB_TOKEN')
    repo = os.getenv('GITHUB_REPOSITORY')
    prefix = ''
    bump = ''

    short_options = "p:b:"
    long_options = ["prefix=", "bump="]

    try:
        arguments, values = getopt.getopt(argv, short_options, long_options)
    except getopt.error as err:
        print (str(err))
        sys.exit(2)

    for current_argument, current_value in arguments:
        if current_argument in ("-p", "--prefix"):
            prefix = current_value
        elif current_argument in ("-b", "--bump"):
            bump = current_value

    client = Github(token, per_page=50)
    repository = client.get_repo(repo)
    releases = repository.get_releases().get_page(0)

    latest_release = ''
    for release in releases:
        release_tag = release.tag_name
        if not release_tag.startswith(prefix):
            continue
        stripped_release = release_tag.removeprefix('v')
        if latest_release == '':
            latest_release = stripped_release
        else:
            if (semver.compare(stripped_release, latest_release) == 1):
                latest_release = stripped_release

    latest = semver.VersionInfo.parse(latest_release)
    next = latest.next_version(part=bump)

    if next.prerelease != None:
        strnext = str(next).replace('-rc.', '-rc')
    
    print('v{}'.format(strnext))

if __name__ == "__main__":
   main(sys.argv[1:])
