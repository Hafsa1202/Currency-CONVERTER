import requests
import json
from datetime import datetime

class CurrencyConverter:
    def __init__(self):
        # Common currency codes
        self.currencies = {
            'USD': 'US Dollar',
            'EUR': 'Euro',
            'GBP': 'British Pound',
            'JPY': 'Japanese Yen',
            'AUD': 'Australian Dollar',
            'CAD': 'Canadian Dollar',
            'CHF': 'Swiss Franc',
            'CNY': 'Chinese Yuan',
            'INR': 'Indian Rupee',
            'PKR': 'Pakistani Rupee',
            'SAR': 'Saudi Riyal',
            'AED': 'UAE Dirham',
            'KRW': 'South Korean Won',
            'SGD': 'Singapore Dollar',
            'HKD': 'Hong Kong Dollar',
            'NZD': 'New Zealand Dollar',
            'SEK': 'Swedish Krona',
            'NOK': 'Norwegian Krone',
            'DKK': 'Danish Krone',
            'RUB': 'Russian Ruble'
        }
    
    def get_exchange_rate(self, from_currency, to_currency):
        """
        Get exchange rate between two currencies
        """
        try:
            # Fetch data from API
            url = f"{self.base_url}{from_currency}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if to_currency in data['rates']:
                return data['rates'][to_currency]
            else:
                print(f"Currency '{to_currency}' not found in exchange rates.")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rates: {e}")
            return None
        except KeyError as e:
            print(f"Invalid currency code: {e}")
            return None
    
    def convert_currency(self, amount, from_currency, to_currency):
        """
        Convert amount from one currency to another
        """
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        
        if from_currency == to_currency:
            return amount
        
        exchange_rate = self.get_exchange_rate(from_currency, to_currency)
        
        if exchange_rate is not None:
            converted_amount = amount * exchange_rate
            return round(converted_amount, 2)
        else:
            return None
    
    def display_available_currencies(self):
        """
        Display all available currencies
        """
        print("\n" + "="*50)
        print("AVAILABLE CURRENCIES")
        print("="*50)
        for code, name in self.currencies.items():
            print(f"{code}: {name}")
        print("="*50)
    
    def get_currency_info(self, currency_code):
        """
        Get currency information
        """
        currency_code = currency_code.upper()
        if currency_code in self.currencies:
            return self.currencies[currency_code]
        else:
            return "Currency not found in our database"
    
    def run_converter(self):
        """
        Main interactive currency converter
        """
        print("="*60)
        print("           WELCOME TO CURRENCY CONVERTER")
        print("="*60)
        print("Convert between different world currencies with live rates!")
        print("Type 'quit' to exit, 'help' for commands, 'list' for currencies")
        print("-"*60)
        
        while True:
            try:
                print("\n" + "-"*40)
                command = input("Enter command (or 'help'): ").strip().lower()
                
                if command == 'quit' or command == 'exit':
                    print("Thank you for using Currency Converter! Goodbye!")
                    break
                
                elif command == 'help':
                    print("\nAVAILABLE COMMANDS:")
                    print("• convert  - Convert currency")
                    print("• list     - Show available currencies")
                    print("• info     - Get currency information")
                    print("• quit     - Exit the program")
                
                elif command == 'list':
                    self.display_available_currencies()
                
                elif command == 'info':
                    currency = input("Enter currency code (e.g., USD): ").strip().upper()
                    info = self.get_currency_info(currency)
                    print(f"\n{currency}: {info}")
                
                elif command == 'convert':
                    # Get conversion details
                    print("\n--- CURRENCY CONVERSION ---")
                    
                    amount_str = input("Enter amount to convert: ").strip()
                    try:
                        amount = float(amount_str)
                        if amount < 0:
                            print("Amount cannot be negative!")
                            continue
                    except ValueError:
                        print("Please enter a valid number!")
                        continue
                    
                    from_currency = input("From currency (e.g., USD): ").strip().upper()
                    to_currency = input("To currency (e.g., EUR): ").strip().upper()
                    
                    if not from_currency or not to_currency:
                        print("Please enter valid currency codes!")
                        continue
                    
                    print("\nConverting... Please wait...")
                    
                    result = self.convert_currency(amount, from_currency, to_currency)
                    
                    if result is not None:
                        from_name = self.get_currency_info(from_currency)
                        to_name = self.get_currency_info(to_currency)
                        
                        print(f"\n{'='*50}")
                        print("CONVERSION RESULT")
                        print(f"{'='*50}")
                        print(f"Amount: {amount:,.2f} {from_currency}")
                        print(f"From: {from_name}")
                        print(f"To: {to_name}")
                        print(f"Result: {result:,.2f} {to_currency}")
                        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                        print(f"{'='*50}")
                        
                        # Show rate
                        rate = self.get_exchange_rate(from_currency, to_currency)
                        if rate:
                            print(f"Exchange Rate: 1 {from_currency} = {rate:.4f} {to_currency}")
                    else:
                        print("Conversion failed. Please check your currency codes and try again.")
                
                else:
                    print("Unknown command. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\n\nExiting... Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

def main():
    """
    Main function to run the currency converter
    """
    converter = CurrencyConverter()
    converter.run_converter()

if __name__ == "__main__":
    # You can also use the converter programmatically:
    
    # Example of direct usage:
    print("="*60)
    print("DIRECT CONVERSION EXAMPLE")
    print("="*60)
    
    converter = CurrencyConverter()
    
    # Convert 100 USD to EUR
    result = converter.convert_currency(100, 'USD', 'EUR')
    if result:
        print(f"100 USD = {result} EUR")
    
    # Convert 50 EUR to GBP
    result = converter.convert_currency(50, 'EUR', 'GBP')
    if result:
        print(f"50 EUR = {result} GBP")
    
    print("\nStarting interactive converter...\n")
    
    # Start interactive mode
    main()
