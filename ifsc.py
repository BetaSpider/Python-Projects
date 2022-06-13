import requests

url="https://ifsc.razorpay.com/"

ifsc=input("Enter the IFSC code:")

res=url+ifsc

getData=requests.get(res).json()

bankName=getData['BANK']
branchName=getData['BRANCH']

print("Bank name is:",bankName)
print("Branch name is:",branchName)