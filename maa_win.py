from win32api import GetFileVersionInfo, LOWORD, HIWORD

def file_version(filename):
    try:
        info = GetFileVersionInfo(filename, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return HIWORD(ms), LOWORD(ms), HIWORD(ls), LOWORD(ls)
    except:
        return 0,0,0,0

def file_version_str(filename, delim="."):
  return (str(delim).join([str(i) for i in file_version(filename)])) 

  
