class MULTIPLEFUNCTIONS():

    def list_sub_fields():
        sub_fields = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for subfields in sub_fields:
            print(subfields)
            end=sub_fields
        return end

    def oddEven():
        number = int(input("Enter a number: "))
        if number%2==0:
            print(f"{number} is even number")
            end=f"{number} is even number"
        else:
            print(f"{number} is odd number")
            end=f"{number} is odd number"
        return end  

    def check_eligibility():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))
        
        if gender.lower() == "male" and age >= 18:
            print("Not Eligible")
            end="Not Eligible"
        else:
            print("Eligible")
            end="Eligible"
        return end 

    def calculate_percentage():
        subject1 = 98
        subject2 = 87
        subject3 = 95
        subject4 = 95
        subject5 = 93

        total=subject1+subject2+subject3+subject4+subject5
        percentage=(total/500)*100
        print("Total:",total)
        end="Total:",total
        print("Percentage:",percentage)
        end="Percentage:",percentage
        return end

    def calculate_triangle():
        height=3
        breadth=4
        area=(height*breadth)/2
        print("Area of Triangle:",area)
        end="Area of Triangle:",area
        height1=3
        height2=4
        breadth=45
        perimeter=height1+height2+breadth
        print("Perimeter of Triangle:",perimeter)
        end="Perimeter of Triangle:",perimeter
        return end
                       