import requests
import warnings
import pandas as pd
warnings.filterwarnings("ignore")

class json_csv:
    
    __final_data = dict()
    column_names = list()
    
    def __init__(self,data, filename, file_type):
        self.data = data
        self.filename = filename
        self.file_type = file_type

    def start(self):
        self.__iter_data()
        self.__column_names()
        self.__sort_columns()
        self.__to_csv()
       
        return "converted"
    
    def __iter_data(self):
        final_data =  dict()
        #columns = []
        if type(self.data) == dict:
            if len(self.data) ==1:
                for key in self.data:
                    if type(self.data[key])==list:
                        break
                    self.data = json_csv.__extract(self.data,key)
                self.data = self.data[key]
        
                    
        for row_num in range(len(self.data)): 
            row = dict()
            for i in self.data[row_num]:  
                temp_dict_1=dict()
                temp_dict_2=dict()
                temp_dict_1 = json_csv.__extract(self.data[row_num],i) 

                if type(temp_dict_1) == dict:
                    for j in temp_dict_1:
                        temp_dict_2 = json_csv.__extract(temp_dict_1,j)
                        row.update(temp_dict_2)
            json_csv.__final_data[row_num] = row
    
    def __extract(element, index):
        
        temp = dict()
        type(element[index])

        if type(element[index]) == list or type(element[index]) == tuple:
            for i in range(len(element[index])):
               
                temp[index+"_"+str(i+1)] = element[index][i]
                
              


        elif type(element[index]) == dict:
            for key in element[index]:
                
                temp[str(index)+"_"+key] = element[index][key]
        else:
            temp[index] = element[index]
        return temp
    
    def __column_names(self):
        columns = set()
        for i in json_csv.__final_data:
            temp=set()
            
            for j in json_csv.__final_data[i]:
                temp.add(j)
            columns=columns.union(temp)
        columns =[column for column in columns]
        columns.sort()
        json_csv.column_names = columns 
    
    def __sort_columns(self):
        for count, i in enumerate(['id','num','name','img','weight']):
            if i in json_csv.column_names:
                temp = json_csv.column_names.pop(json_csv.column_names.index(i))
                json_csv.column_names.insert(count,temp)
    
    def __to_csv(self):
        df = pd.DataFrame(columns = json_csv.column_names)
        for i in json_csv.__final_data:
            df_temp = pd.DataFrame(json_csv.__final_data[i], index=[i],columns =json_csv.column_names)
            df=df.merge(df_temp, how = "outer")
        df.dropna(axis=1, how='all', inplace=True)
        
        if self.file_type == 1:
            df.to_csv(self.filename+".csv", index= False)
        else:
            df.to_excel(self.filename+".xlsx", index= False)

if __name__ =="__main__":
    while(True):
        print("enter url \n")
        url = input()
        if url.endswith('.json'):
            while True:
                print("Enter \n1 for json to .csv\n2 for json to .xlsx\n")
                file_type = int(input())
                if file_type in [1,2]:
                    while True:
                        print("Enter file name without .format")
                        file_name = input()
                        if len(file_name) == 0:
                            print("file name is None enter valid file name")
                            continue
                        else:
                            
                            break
                        break
                else:
                    print("Enter correct file return format 1 or 2")
                    continue
                break
        else:
            print("Enter correct file name with .json ending")
            continue
        break
    #url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
    response = requests.get(url)
    if response.status_code == 200:
        dataa = response.json()
        print("Data Grabbed")
    else:
        print("Error:", response.status_code)
    run = json_csv(dataa,file_name, file_type)
    print(run.start())
