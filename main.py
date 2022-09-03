import installerBase

def make_directory_structure():
    pass


exe_url = 'https://www.google.com/'
final_exe_pos = '/'
name = 'Demo'
size = '100 bajillion gigabytes'
timeout = 1
download_attempts = 10

if __name__ == '__main__':
    installerBase.Installer(exe_url, final_exe_path=final_exe_pos, name=name, size=size,
                            timeout=timeout, download_attempts=download_attempts)
