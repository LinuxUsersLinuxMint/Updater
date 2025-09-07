import configparser, requests

updater_config = configparser.ConfigParser()
updater_config.read("UpdaterSettings/updater.ini")

update_mode = updater_config["UpdateMode"]["update_mode"]
releases_tag = updater_config["UpdateMode"]["releases_tag"]

file_name = updater_config["DownloadFileSettings"]["file_name"]
file_url = updater_config["DownloadFileSettings"]["file_url"]
chunk_size = int(updater_config["DownloadFileSettings"]["chunk_size"])
update_check_url = updater_config["UpdateCheckSettings"]["update_check_url"]
current_ver_file = updater_config["UpdateCheckSettings"]["current_ver_file"]
update_folder_name = updater_config["Folder"]["update_folder_name"]

check = requests.get(update_check_url)
new_ver = check.text

releases_tag += new_ver

if update_mode == "release":
    github_name = updater_config["GithubAccount"]["github_name"]
    github_repository_name = updater_config["GithubAccount"]["github_repository_name"]
    file_url = "https://github.com/" + github_name + "/" + github_repository_name + "/releases/download/" + releases_tag + "/" + file_name