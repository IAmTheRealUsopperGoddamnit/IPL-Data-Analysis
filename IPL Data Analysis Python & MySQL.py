import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#Data Analysis of IPL Matches from 2008-2020.

match=pd.read_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/matchpython.csv')
matchdf=pd.DataFrame(match)
matchcolumn=['id','city','date','player_of_match','venue','neutral_venue','team1','team2','toss_winner','toss_decision','winner','result','result_margin','eliminator','method','umpire1','umpire2']

mydb=mysql.connector.connect(host="localhost",user="root",passwd="cYBeRcIty!^#",port=3306)
mycursor=mydb.cursor()
mycursor.execute("drop database ipl")
mycursor.execute("create database ipl")

mydb=mysql.connector.connect(host="localhost",user="root",passwd="cYBeRcIty!^#",database="ipl", port=3306)
mycursor=mydb.cursor()
mycursor.execute("""create table matches(
id int PRIMARY KEY,
city VARCHAR(40),
match_date DATE,
player_of_match VARCHAR(30),
venue VARCHAR(60),
neutral_venue INT,
team1 VARCHAR(35),
team2 VARCHAR(35),
toss_winner VARCHAR(35),
toss_decision VARCHAR(10),
winner VARCHAR(35),
result VARCHAR(15),
result_margin VARCHAR(5) NULL,
eliminator VARCHAR(5),
method VARCHAR(5) NULL,
umpire1 VARCHAR(25),
umpire2 VARCHAR(25))""")

print('Created the table.')

mydb=mysql.connector.connect(host="localhost",user="root",passwd="cYBeRcIty!^#",database="ipl", port=3306)
mycursor=mydb.cursor()
mycursor.execute("""
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/matchsql.csv'
INTO TABLE matches
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
""")
mydb.commit()
print(mycursor.rowcount,"Record Inserted")

print("WELCOME TO DATA ANALYSIS OF IPL MATCHES FROM 2008-2020")

YesNo=input("Do you want to display all the records? (Yes/No)")
if YesNo=='Yes':
    print(matchdf)
else:
    print("No records are displayed.")

def main():
    
    print("General Analytics of IPL Matches Played from 2008-2020")

    print('Options')
    print('1: Player of the Match Awards')
    print('2: Number of Matches Won by an IPL Team')
    print('3: Number of Matches Played by an IPL Team')
    print('4: Number of Toss Wins of an IPL Team')
    print('5: Number of IPL Matches Played in a City')
    print('6: Result Margin Distribution')
    print('7: Number of IPL Matches Played in a Stadium')
    print('8: Number of Matches Umpired by an Umpire')
    Input=int(input("Enter a number: "))
    if Input==1:
        print("Most Player of the Match Awards won by")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="cYBeRcIty!^#",database="ipl", port=3306)
        mycursor=mydb.cursor()
        mycursor.execute("select player_of_match from matches where player_of_match='AB de Villiers' LIMIT 1")
        for x in mycursor:
            print(x)
        PlayerList=matchdf.player_of_match.unique()
        CleanedPlayerList=[x for x in PlayerList if x==x]
        List=[]
        for x in range(0,233,1):
            YoyoList=CleanedPlayerList[x]
            Yoyo=matchdf['player_of_match'].value_counts()[YoyoList]
            List.append(int(Yoyo))
        df=pd.DataFrame(List,CleanedPlayerList)
        df.plot(kind='bar', title='Player of the Match Awards', xlabel='Player', ylabel='Awards', color='b')
        plt.show()
    elif Input==2:
        print("Most Matches Won by")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="cYBeRcIty!^#",database="ipl", port=3306)
        mycursor=mydb.cursor()
        mycursor.execute("select winner from matches where winner='Mumbai Indians' LIMIT 1")
        for x in mycursor:
            print(x)
        WinnerList=matchdf.winner.unique()
        CleanedWinnerList=[x for x in WinnerList if x==x]
        List=[]
        for x in range(0,15,1):
            YoyoList=CleanedWinnerList[x]
            Yoyo=matchdf['winner'].value_counts()[YoyoList]
            List.append(int(Yoyo))
        df=pd.DataFrame(List,CleanedWinnerList)
        df.plot(kind='bar', title='Number of Matches Won by an IPL Team', xlabel='Team', ylabel='Wins', color='g')
        plt.show()
    elif Input==3:
        print("Most Matches Played by")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="cYBeRcIty!^#",database="ipl", port=3306)
        mycursor=mydb.cursor()
        mycursor.execute("select team1 from matches where team1='Royal Challengers Bangalore' LIMIT 1")
        for x in mycursor:
            print(x)
        TeamList=matchdf.team1.unique()
        CleanedTeamList=[x for x in TeamList if x==x]
        List=[]
        for x in range(0,15,1):
            YoyoList=CleanedTeamList[x]
            Yoyo=matchdf['team1'].value_counts()[YoyoList]
            List.append(int(Yoyo))
        df=pd.DataFrame(List,CleanedTeamList)
        df.plot(kind='bar', title='Number of Matches Played by an IPL Team', xlabel='Team', ylabel='Matches Played', color='r')
        plt.show()
    elif Input==4:
        print("Most Tosses Won by")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="cYBeRcIty!^#",database="ipl", port=3306)
        mycursor=mydb.cursor()
        mycursor.execute("select toss_winner from matches where toss_winner='Mumbai Indians' LIMIT 1")
        for x in mycursor:
            print(x)
        TossWinnerList=matchdf.toss_winner.unique()
        CleanedTossWinnerList=[x for x in TossWinnerList if x==x]
        List=[]
        for x in range(0,15,1):
            YoyoList=CleanedTossWinnerList[x]
            Yoyo=matchdf['toss_winner'].value_counts()[YoyoList]
            List.append(int(Yoyo))
        df=pd.DataFrame(List,CleanedTossWinnerList)
        df.plot(kind='bar', title='Number of Toss Wins of an IPL Team', xlabel='Team', ylabel='Toss Wins', color='c')
        plt.show()
    elif Input==5:
        print("Most Matches Played in")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="cYBeRcIty!^#",database="ipl", port=3306)
        mycursor=mydb.cursor()
        mycursor.execute("select city from matches where city='Mumbai' LIMIT 1")
        for x in mycursor:
            print(x)
        CityList=matchdf.city.unique()
        CleanedCityList=[x for x in CityList if x==x]
        Values=[matchdf['city'].value_counts()['Bangalore'],matchdf['city'].value_counts()['Chandigarh'],matchdf['city'].value_counts()['Delhi'],matchdf['city'].value_counts()['Mumbai'],
                matchdf['city'].value_counts()['Kolkata'],matchdf['city'].value_counts()['Jaipur'],matchdf['city'].value_counts()['Hyderabad'],matchdf['city'].value_counts()['Chennai'],
                matchdf['city'].value_counts()['Cape Town'],matchdf['city'].value_counts()['Port Elizabeth'],matchdf['city'].value_counts()['Durban'],matchdf['city'].value_counts()['Centurion'],
                matchdf['city'].value_counts()['East London'],matchdf['city'].value_counts()['Johannesburg'],matchdf['city'].value_counts()['Kimberley'],matchdf['city'].value_counts()['Bloemfontein'],
                matchdf['city'].value_counts()['Ahmedabad'],matchdf['city'].value_counts()['Cuttack'],matchdf['city'].value_counts()['Nagpur'],matchdf['city'].value_counts()['Dharamsala'],
                matchdf['city'].value_counts()['Kochi'],matchdf['city'].value_counts()['Indore'],matchdf['city'].value_counts()['Visakhapatnam'],matchdf['city'].value_counts()['Pune'],
                matchdf['city'].value_counts()['Raipur'],matchdf['city'].value_counts()['Ranchi'],matchdf['city'].value_counts()['Abu Dhabi'],matchdf['city'].value_counts()['Rajkot'],
                matchdf['city'].value_counts()['Kanpur'],matchdf['city'].value_counts()['Bengaluru'],matchdf['city'].value_counts()['Dubai'],matchdf['city'].value_counts()['Sharjah']]
        df=pd.DataFrame(Values,CleanedCityList)
        df.plot(kind='bar', title='Number of IPL Matches Played in a City', xlabel='City', ylabel='Matches', color='m')
        plt.show()
    elif Input==6:
        MarginList=matchdf.result_margin.unique()
        CleanedMarginList=[x for x in MarginList if x==x]
        List=[]
        for x in range(0,91,1):
            YoyoList=CleanedMarginList[x]
            Yoyo=matchdf['result_margin'].value_counts()[YoyoList]
            List.append(int(Yoyo))
        df=pd.DataFrame(List,CleanedMarginList)
        df.plot(kind='line', title='Result Margin Distribution', xlabel='Result Margin', ylabel='Matches', color='k')
        plt.show()
    elif Input==7:
        print("Most Matches Played in")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="cYBeRcIty!^#",database="ipl", port=3306)
        mycursor=mydb.cursor()
        mycursor.execute("select venue from matches where venue='Eden Gardens' LIMIT 1")
        for x in mycursor:
            print(x)
        VenueList=matchdf.venue.unique()
        CleanedVenueList=[x for x in VenueList if x==x]
        List=[]
        for x in range(0,36,1):
            YoyoList=CleanedVenueList[x]
            Yoyo=matchdf['venue'].value_counts()[YoyoList]
            List.append(int(Yoyo))
        df=pd.DataFrame(List,CleanedVenueList)
        df.plot(kind='bar', title='Number of IPL Matches Played in a Stadium', xlabel='Venue', ylabel='Matches', color='chartreuse')
        plt.show()
    elif Input==8:
        print("Most Popular Umpire is")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="cYBeRcIty!^#",database="ipl", port=3306)
        mycursor=mydb.cursor()
        mycursor.execute("select umpire1 from matches where umpire1='HDPK Dharmasena' LIMIT 1")
        for x in mycursor:
            print(x)
        UmpireList=matchdf.umpire1.unique()
        CleanedUmpireList=[x for x in UmpireList if x==x]
        List=[]
        for x in range (0,48,1):
            YoyoList=CleanedUmpireList[x]
            Yoyo=matchdf['umpire1'].value_counts()[YoyoList]
            List.append(int(Yoyo))
        df=pd.DataFrame(List,CleanedUmpireList)
        df.plot(kind='bar', title='Number of Matches Umpired by an Umpire', xlabel='Umpire', ylabel='Matches', color='#6633FF')
        plt.show()

    Restart=input("Do you want to run the program again? (Yes/No)")
    if Restart=="Yes":
        main()
    else:
        exit()
main()
