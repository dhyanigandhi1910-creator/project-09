import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
class SalesDataAnalyzer:
    def __init__(self,file_path=None):
        self.data=None
        if file_path:
            self.load_data(file_path)
    
    def load_data(self,file_path):
        try:
            print("== Load Dataset ==")
            self.data=pd.read_csv(file_path)
            print("Dataset loaded successfully")
        except Exception as e:
            print("error loading dataset:",e)

    def explore_data(self):
        if self.data is not None:
            print("==explore data==")
            print("\n 1.display first 5 rows\n 2.display last 5 rows\n 3.display column name\n 4.display data type\n 5.display basic info")
            choice=int(input("enter your choice: "))
            if choice==1:
                print(self.data.head())
            elif choice==2:
                print(self.data.tail())
            elif choice==3:
                for col in self.data:
                    print(col)
            elif choice==4:
                print(self.data.dtypes)
            elif choice==5:
                print(self.data.info())
            else:
                print("invalid choice")
        else:
                print("no dataset loaded")
        
    def perform_operations(self):
        if self.data is not None:
            print("==perform dataframe operation==")
            print("1. Add new column (Profit Margin)")
            print("2. Increase Sales by 10%")
            print("3. Sort by Sales")
            print("4. Filter by Region")
            choice = int(input("Enter your choice: "))
            if choice==1:
                self.data["totalsalary_with_bonus"]=self.data["Salary"]+self.data["Bonus_Amount"]
                print("new column added\n ",self.data.head())
            elif choice==2:
                self.data["Sales_Q1"]=self.data["Sales_Q1"]*1.1
                print("Sales increased by 10%!\n", self.data.head())
            elif choice == 3:
                print(self.data.sort_values(by="Total_Sales", ascending=False))
            elif choice == 4:
                region = input("Enter region name: ")
                print(self.data[self.data["Region"] == region])
            else:
                print("Invalid choice!")
        else:
            print("No dataset loaded!")
    
    def handle_missing_data(self):
        if self.data is not None:
            print("\n== Handle Missing Data ==")
            print("Missing values per column:\n", self.data.isnull().sum())
            self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
            print("Missing values handled (filled with mean).")
        else:
            print("No dataset loaded!")

    def descriptive_statistics(self):
        if self.data is not None:
            print("\n== Descriptive Statistics ==")
            print(self.data.describe())
        else:
            print("No dataset loaded!")

    def visualize_data(self):
        if self.data is not None:
            print("\n== Data Visualization ==")
            print("1.Bar\n2.Line\n3.Scatter\n4.Pie\n5.Histogram ")
            choice=int(input("enter yoyr choice: "))
            if choice == 1:
                print("\n***Bar Chart***")
                print("This chart shows total sales for each department.")
                self.data.groupby("Department")["Total_Sales"].sum().plot(kind="bar",label="Total Sales",color='green')
                plt.title("Total Sales by Department")
                plt.xlabel("Department")
                plt.ylabel("Total Sales")
                plt.xticks(rotation=45)
                plt.legend(loc="upper left")
                plt.show()
            elif choice == 2:
                print("\n***Line Chart***")
                print("This chart shows sales trend over years.")
                self.data['Join_Date'] = pd.to_datetime(self.data['Join_Date'])
                self.data.groupby(self.data['Join_Date'].dt.to_period('Y'))['Total_Sales'].sum().plot(kind="line",marker='o')
                plt.title(" TotalSales Trend by Year")
                plt.xlabel("year")
                plt.ylabel("Total Sales")
                plt.xticks(rotation=45)
                plt.show()
            elif choice == 3:
                print("\n***Scatter Plot***")
                print("This chart shows relationship between department and salary.")
                sns.scatterplot(x="Department", y="Salary", data=self.data)
                plt.xlabel("Department")
                plt.ylabel("Salary")
                plt.title("Department vs Salary")
                plt.show()
            elif choice == 4:
                print("\n***Pie Chart***")
                print("This chart shows percentage of sales by region.")
                self.data.groupby("Region")["Total_Sales"].sum().plot(kind="pie", autopct="%1.1f%%")
                plt.title("Sales by Region")
                plt.show()
            elif choice == 5:
                print("\n***Histogram***")
                print("This chart shows distribution of employee salaries.")
                self.data["Salary"].plot(kind="hist", bins=5)
                plt.title("Salary Distribution")
                plt.show()
        else:
            print("No dataset loaded!")

    def save_visualization(self, filename="plot.png"):
        plt.savefig(filename)
        print(f"Visualization saved as {filename} successfully!")

def main():
    analyzer = SalesDataAnalyzer()
    while True:
        print("\n========== Data Analysis & Visualization Program ==========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            path = input("Enter dataset path (CSV): ")
            analyzer.load_data(path)
        elif choice == 2:
            analyzer.explore_data()
        elif choice == 3:
            analyzer.perform_operations()
        elif choice == 4:
            analyzer.handle_missing_data()
        elif choice == 5:
            analyzer.descriptive_statistics()
        elif choice == 6:
            analyzer.visualize_data()
        elif choice == 7:
            filename = input("Enter filename (e.g., plot.png): ")
            analyzer.save_visualization(filename)
        elif choice == 8:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()


















        
   
        

    



            

                  