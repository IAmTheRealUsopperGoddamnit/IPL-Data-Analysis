import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#Data Analysis of IPL Matches from 2008-2020.

match=pd.read_csv('C:/Users/amucr/OneDrive/Documents/Code/Reference Files/match.csv')
matchdf=pd.DataFrame(match)
matchcolumn=['id','city','date','player_of_match','venue','neutral_venue','team1','team2','toss_winner','toss_decision','winner','result','result_margin','eliminator','method','umpire1','umpire2']

mydb=mysql.connector.connect(host="localhost",user="root",passwd="C++TheySaidItCouldNotBeDone1",port=3306)
mycursor=mydb.cursor()
mycursor.execute("create database ipl")

mydb=mysql.connector.connect(host="localhost",user="root",passwd="C++TheySaidItCouldNotBeDone1",database="ipl", port=3306)
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

mydb=mysql.connector.connect(host="localhost",user="root",passwd="C++TheySaidItCouldNotBeDone1",database="ipl", port=3306)
mycursor=mydb.cursor()
mycursor.execute("""
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/match.csv'
INTO TABLE matches
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
""")
mydb.commit()
print(mycursor.rowcount,"Record Inserted")

#import mysql.connector
#mydb=mysql.connector.connect(host="localhost",user="root",passwd="C++TheySaidItCouldNotBeDone1",database="ipl", port=3306)
#mycursor=mydb.cursor()
#mycursor.execute("Select * from matches")
#for x in mycursor:
#    print(x)

print("WELCOME TO DATA ANALYSIS OF IPL MATCHES FROM 2008-2020")

YesNo=input("Do you want to display all the records? (Yes/No)")
if YesNo=='Yes':
    print(matchdf)
else:
    print("No records are displayed.")

print("General Analytics of IPL Matches Played from 2008-2020")

print('Options')
print('1: Most Player of the Match Awards')
print('2: Team With Most IPL Wins')
print('3: Team Which Played in Most IPL Matches')
print('4: Team With Most Toss Wins')
print('5: City With Most IPL Matches')
print('6: Result Margin Distribution')
print('7: Commonest Venue')
print('8: Commonest Umpire')
Input=int(input("Enter a number: "))
if Input==1:
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="C++TheySaidItCouldNotBeDone1",database="ipl", port=3306)
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
    df.plot(kind='bar', title='Most Player of Matches', xlabel='Players', ylabel='Player of Matches', color='b')
    plt.show()
elif Input==2:
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="C++TheySaidItCouldNotBeDone1",database="ipl", port=3306)
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
    df.plot(kind='bar', title='Team With Most IPL Wins', xlabel='Teams', ylabel='Wins', color='g')
    plt.show()
elif Input==3:
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="C++TheySaidItCouldNotBeDone1",database="ipl", port=3306)
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
    df.plot(kind='bar', title='Team with Most IPL Matches', xlabel='Teams', ylabel='Matches Played In', color='r')
    plt.show()
elif Input==4:
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="C++TheySaidItCouldNotBeDone1",database="ipl", port=3306)
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
    df.plot(kind='bar', title='Team With Most Toss Wins', xlabel='Teams', ylabel='Toss Wins', color='c')
    plt.show()
elif Input==5:
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="C++TheySaidItCouldNotBeDone1",database="ipl", port=3306)
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
    df.plot(kind='bar', title='City With Most IPL Matches', xlabel='Cities', ylabel='IPL Matches Played', color='m')
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
    df.plot(kind='line', title='Result Margin Distribution', xlabel='Result Margin', ylabel='Frequency', color='k')
    plt.show()
elif Input==7:
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="C++TheySaidItCouldNotBeDone1",database="ipl", port=3306)
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
    df.plot(kind='bar', title='Commonest Venue', xlabel='Venue', ylabel='IPL Matches Played', color='chartreuse')
    plt.show()
elif Input==8:
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="C++TheySaidItCouldNotBeDone1",database="ipl", port=3306)
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
    df.plot(kind='bar', title='Commonest Umpire', xlabel='Umpire', ylabel='IPL Matches Umpired In', color='#6633FF')
    plt.show()
