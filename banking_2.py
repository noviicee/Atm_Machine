#20-01-2021

import sys
class Atm:
	def __init__(self):
		self.__pin=""
		self.__balance=0.00

		self.menu()
	def menu(self):
		option=int(input("""
			Hello!
			Select your option-
			1. Add Bank and Create Pin
			2. Check Balance
			3. Deposit
			4. Withdrawal
			5. Exit

			"""))
		if option==1:
			self.create_pin()
		elif option==2:
			self.check_balance()
		elif option==3:
			self.deposit()
		elif option==4:
			self.withdraw()
		elif option==5:
			print("Thanks for using our application :)")
			sys.exit(0)
		else:
			print("Please select a valid option and try again later.")

	def create_pin(self):
		input("Enter your bank's name:")
		user_name=input("Enter your username:")
		pin=input("Enter your pin to create:")
		self.__pin=pin
		print("\nHello",user_name.title(),"!\nYour pin has been added successfully.")
		self.menu()
	def check_balance(self):
		temp=input("Enter your pin:")
		if temp==self.__pin:
			print("Your current balance is:INR",self.__balance)
		else:
			print("Wrong pin entered, please try again later")
		self.menu()
	def deposit(self):
		temp=input("Enter your pin:")
		if temp==self.__pin:
			amount=float(input("Enter amount to deposit:"))
			self.__balance+=amount
			print("Amount deposited successfully.")
		else:
			print("You have entered the incorrect pin, try again later.")
		self.menu()
	def withdraw(self):
		amount=float(input("Enter amount to withdraw:"))
		temp=input("Enter your pin:")
		if temp==self.__pin:
			if self.__balance<amount:
				print("You don't have suficient amount to withdraw.")
			else:
				self.__balance-=amount
				print("Amount Withdrawal successfull.")
				print("Remaining Balance=INR",self.__balance)
		else:
			print("You have entered the incorrect pin, try again later.")
		self.menu()
sbi=Atm()