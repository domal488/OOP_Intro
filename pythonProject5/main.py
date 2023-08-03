
from imputeation.imputers import MeanImputer


if __name__ == "__main__":

    x = [1, 2, 3, None]
    imputer = MeanImputer()
    imputer.fit(x)
    print(imputer.mean)
    y- imputer.transform([7, 5, None, None])
    print(y)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#Napis kod, który w liście zawierającej liczby i wartości `None` zamienia wartości `None` na średnią z obecnych w liście liczb.
# Przykłądowo [1,2,3,None] -> [1,2,3,2]

