![image](https://user-images.githubusercontent.com/82535503/167408437-51562cf7-7d50-4999-b2b8-63e2aea890c5.png)


# choco-addon
This is a addon to the choco-package manager forexternal downloads.


## Supports:
| Operating         |     System        |    
| -------------     | -------------     |
| Windows           |         ✅         |
| Linux             |     ❌  |
| MacOS             |     ❌  |

you can easily manipulate the code to work for these platforms but atm I just do not use linux and I dont have a mac


##  How It Works?
- You have 3 files to currently work with : `choco.t`, `zip.t` and `exe.t`
- In `choco.t` add the application names to download.
- In `zip.t` add direct download links for your desired `.zip` files
- In `exe.t` add direct download links for your want `.exe` files
- run `python main.py`
