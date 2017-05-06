# QuakeCL [![Build Status](https://travis-ci.org/amitness/QuakeCL.svg?branch=master)](https://travis-ci.org/amitness/QuakeCL)
View the 5 recent **earthquakes** that took place in **Nepal** in your terminal.

![Screenshot](https://1.bp.blogspot.com/-VqSshLgpYUs/V8MZTsR7fPI/AAAAAAAACxc/_XiZkz2tlgsqjh0veID2elAYZWxzaAwxQCLcB/s1600/Screenshot%2Bfrom%2B2016-08-28%2B22%253A31%253A38.png)

### INSTALLATION:
#### One Step Installation
```
wget -q -O - https://raw.githubusercontent.com/amitness/QuakeCL/master/install.sh | sudo bash
```

#### Manual Installation
- Clone the repository
     
     ```git clone https://github.com/amitness/QuakeCL```

- Run the installation script inside the cloned folder
     ```bash
     chmod a+x install.sh
     sudo ./install.sh
     ```
     
### USAGE:
    ~ $ earthquake 

### Built with:
 * Python
 * [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1eeIOB58Dn5qRNWTySqrL35U8xY3JjZ7yhg5Dpxvbz8s/edit) for scraping the data using `IMPORTXML` and `XPath`


### References
 * Data from [National Seismological Centre](http://www.seismonepal.gov.np)
