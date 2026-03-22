import json
import urllib.request

print("GitHub Repository Analyser")

owner = input("Enter the repository owner: ")
repoName = input("Enter the name of the repository: ")

url = f"https://api.github.com/repos/{owner}/{repoName}"

try:
    with urllib.request.urlopen(url) as response:
        status = response.getcode()
        print("Status Code:", status)

        if status == 200:
            # The Repo information
            data = json.loads(response.read().decode())

            print("\nRepository Information")
            print("__________________________________")
            print("Name:", data["name"])
            print("Description:", data["description"])
            print("Stars:", data["stargazers_count"])
            print("Forks:", data["forks_count"])
            print("Open Issues:", data["open_issues_count"])

            # Languages
            print("\nLanguages used:")
            languages_url = data["languages_url"]
            with urllib.request.urlopen(languages_url) as lang_response:
                lang_data = json.loads(lang_response.read().decode())
                for language in lang_data:
                    print("-", language)

            # Contributors
            print("\nTop Contributors:")
            contributors_url = data["contributors_url"]
            with urllib.request.urlopen(contributors_url) as contrib_response:
                contrib_data = json.loads(contrib_response.read().decode())

                if contrib_data:
                    for contributor in contrib_data[:5]:  # limit to top 5
                        print("-", contributor["login"], "| Contributions:", contributor["contributions"])
                else:
                    print("No contributors found.")

        else:
            print("Repository not found")

except Exception as e:
    print("An error occurred:", e)
    