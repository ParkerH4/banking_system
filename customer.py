class Customer:
    def __init__(self, Customer_ID, FName, LName, Email, Phone, Address, Date_Of_Birth):
        self.Customer_ID = Customer_ID
        self.FName = FName
        self.LName = LName
        self.Email = Email
        self.Phone = Phone
        self.Address = Address
        self.Date_Of_Birth = Date_Of_Birth

    def __repr__(self):
        return f"Customer({self.Customer_ID}, {self.FName}, {self.LName})"

    def display_info(self):
        return (
            f"Customer ID: {self.Customer_ID}\n"
            f"Name: {self.FName} {self.LName}\n"
            f"Email: {self.Email}\n"
            f"Phone: {self.Phone}\n"
            f"Address: {self.Address}\n"
            f"Date of Birth: {self.Date_Of_Birth}\n"
        )

    def display_accounts(self):
        return self.accounts.display_accounts()

    def display_loans(self):
        return self.loans.display_loans()
