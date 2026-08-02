import getpass
import sys

print(r"""
  _______  __  .___________.  ______  __       __ 
 /  _____||  | |           | /      ||  |     |  |
|  |  __  |  | `---|  |----`|  ,----'|  |     |  |
|  | |_ | |  |     |  |     |  |     |  |     |  |
|  |__| | |  |     |  |     |  `----.|  `----.|  |
 \______| |__|     |__|      \______||_______||__|

""")

print(" Welcome to GitCLI Setup!")
print(" ------------------------")


username = input(" Enter your GitHub Username: ").strip()


print("\n To connect, you need a GitHub Personal Access Token (PAT).")
print(" (Create one at: https://github.com/settings/tokens)")
print(" Note: The characters will be hidden as you paste/type for security.")

token = getpass.getpass(" Enter your GitHub Token: ").strip()


if not username or not token:
    print("\n[Error] Username and Token cannot be empty!")
    sys.exit(1)

print(f"\n[Success] Credentials captured securely for user: {username}!")
