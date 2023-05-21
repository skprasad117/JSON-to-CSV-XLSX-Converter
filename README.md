# JSON to CSV/XLSX Converter

This Python program fetches JSON data from a given URL and converts it into either a CSV or XLSX file format. The program provides a prompt to enter the data link, file type, and file name, and returns the converted file with the specified data.

**Note: While this program is intended to be general and work with any JSON link, it has been thoroughly tested and works best with the following two data sources:**

1. [NASA Open Data API](https://data.nasa.gov/resource/y77d-th95.json)
2. [PokemonGO Pokedex JSON](https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json)

## Why Not Use a Library?

While there are libraries available, such as `pandas`, that provide convenient methods for converting JSON to CSV/XLSX, this program was designed to demonstrate a manual approach for educational purposes. By implementing the conversion process without relying on a library, it helps users understand the underlying logic and steps involved in the conversion.

By writing the conversion code manually, it allows users to have more control over the process and customize it as needed. Additionally, it reduces dependencies on external libraries, making the program more lightweight and easier to understand and maintain.

However, it's important to note that using a library like `pandas` can offer more robust and efficient solutions for handling JSON data conversion. If you prefer a more streamlined approach, it's recommended to explore available libraries that provide specific functionality tailored to JSON conversion.

**Note: As it obsered libraries like pandas are not able to go much deeper in data by its own and resulted in lessure number of features  as compared to my solution, so for more control custom codes can be preferred for larger and complex datasets**

E.g. 
For the https://data.nasa.gov/resource/y77d-th95.json data pandas `.read_json()` resulted in 12 features:
```
'name', 'id', 'nametype', 'recclass', 'mass', 'fall', 'year', 'reclat','reclong','geolocation', ':@computed_region_cbhk_fwbd',':@computed_region_nnqa_25f4'
```
and my code resulted in 14 features: 
```
'id',':@computed_region_cbhk_fwbd','name',':@computed_region_nnqa_25f4','fall','geolocation_coordinates_1','geolocation_coordinates_2','geolocation_type','mass','nametype','recclass','reclat','reclong','year'
 ```
## Installation

1. Clone the repository or download the source code files.
2. Make sure you have Python 3.x installed on your system.
3. Install the required dependencies by running the following command:

```shell
pip install -r requirements.txt
```
## Usage
1. Run the Python script using the command:
```shell
python main.py
```
2. Enter the data link when prompted. Ensure that the URL contains valid JSON data.
3. Choose the desired file type by entering 1 for 'csv' or 2 for 'xlsx' when prompted.
4. Provide a file name (without the file extension) for the converted file.
5. The program will convert the JSON data and save it as a CSV or XLSX file in the current directory.

## Example
Here's an example usage of the program:
```shell
enter url 

https://data.nasa.gov/resource/y77d-th95.json

Enter 
1 for json to .csv
2 for json to .xlsx

1
Enter file name without .format
nasa_meteroite_converted_json_csv
```

## Notes
- Ensure that the provided URL contains valid JSON data; otherwise, the program may not function correctly.
- The program uses the requests library to fetch JSON data from the URL and the pandas library to convert and save the data as CSV or XLSX.
- The program requires an active internet connection to fetch the JSON data.
- Please make sure you have the necessary permissions to write files to the current directory.

## Contributing
Contributions to the project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
