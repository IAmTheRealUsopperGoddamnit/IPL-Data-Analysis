import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#Data Analysis of IPL Matches from 2008-2020.

match=pd.read_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/matchpython.csv')
matchdf=pd.DataFrame(match)
matchcolumn=['id','city','date','player_of_match','venue','neutral_venue','team1','team2','toss_winner','toss_decision','winner','result','result_margin','eliminator','method','umpire1','umpire2']

def main():

    print("DATA ANALYSIS OF IPL MATCHES FROM 2008-2020")
    
    print("Press 1 to see General Analytics of IPL.")
    print("Press 2 to filter IPL matches by attribute.")
    print("Press 3 to sort IPL matches by attribute.")
    INPUT=int(input("Enter a number: "))

    if INPUT==1:
        print('Options')
        print('1: Player of the Match Awards')
        print('2: Number of Matches Won by an IPL Team')
        print('3: Number of Matches Played by an IPL Team')
        print('4: Number of Toss Wins of an IPL Team')
        print('5: Number of IPL Matches Played in a City')
        print('6: Result Margin Distribution')
        print('7: Number of IPL Matches Played in a Stadium')
        print('8: Number of Matches Umpired by an Umpire')
        Input=int(input('Enter a Number: '))
        if Input==1:
            PlayerList=matchdf.player_of_match.unique()
            CleanedPlayerList=[x for x in PlayerList if x==x]
            List=[]
            for x in range(0,233,1):
                YoyoList=CleanedPlayerList[x]
                Yoyo=matchdf['player_of_match'].value_counts()[YoyoList]
                List.append(int(Yoyo))
            df=pd.DataFrame(List,CleanedPlayerList)
            df.plot(kind='bar', title='Player of the Match Awards', xlabel='Players', ylabel='Awards', color='b')
            plt.show()
        elif Input==2:
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
            
    elif INPUT==2:
        print('Filter IPL Matches By')
        print("Options: ")
        print((', '.join(matchcolumn)))
        Input=input('ENTER HERE: ')
        if Input=='id':
            ID=int(input('Input ID: '))
            print(matchdf.loc[matchdf['id']==ID])
        elif Input=='city':
            City=input('Input City Name: ')
            print(matchdf.loc[matchdf['city']==City])
        elif Input=='date':
            Date=input('Input Date (YY-mm-dd): ')
            print(matchdf.loc[matchdf['date']==Date])
        elif Input=='player_of_match':
            Player=input('Input Player Name: ')
            print(matchdf.loc[matchdf['player_of_match']==Player])
        elif Input=='venue':
            Venue=input('Input Venue Name: ')
            print(matchdf.loc[matchdf['venue']==Venue])
        elif Input=='neutral_venue':
            NeutralVenue=int(input("Enter 0 or 1: "))
            print(matchdf.loc[matchdf['neutral_venue']==NeutralVenue])
        elif Input=='team1' or Input=='team2':
            Team=input('Input Team Name: ')
            print(matchdf.loc[matchdf['team1']==Team])
            print(matchdf.loc[matchdf['team2']==Team])
        elif Input=='toss_winner':
            TossWinner=input('Input Toss Winner: ')
            print(matchdf.loc[matchdf['toss_winner']==TossWinner])
        elif Input=='toss_decision':
            TossDecision=input('Input Toss Decision (bat or field): ')
            print(matchdf.loc[matchdf['toss_decision']==TossDecision])
        elif Input=='winner':
            Winner=input('Input Winner Team: ')
            print(matchdf.loc[matchdf['winner']==Winner])
        elif Input=='result':
            Result=input('Input Result (runs or wickets): ')
            print(matchdf.loc[matchdf['result']==Result])
        elif Input=='result_margin':
            ResultMargin=int(input('Input Result Margin: '))
            print(matchdf.loc[matchdf['result_margin']==ResultMargin])
        elif Input=='eliminator':
            Eliminator=input('Input Eliminator (Y for Yes, N for No): ')
            print(matchdf.loc[matchdf['eliminator']==Eliminator])
        elif Input=='method':
            Method=input('Input Method (D/L for Duckworth–Lewis–Stern method): ')
            print(matchdf.loc[matchdf['method']==Method])
        elif Input=='umpire1' or Input=='umpire2':
            Umpire=input('Input Umpire Name: ')
            print(matchdf.loc[matchdf['umpire1']==Umpire])
            print(matchdf.loc[matchdf['umpire2']==Umpire])

    elif INPUT==3:
        print('Sort IPL Matches By')
        print("Options: ")
        print((', '.join(matchcolumn)))
        Input=input('ENTER HERE: ')
        Order=input('ENTER Order of Sorting (Ascending OR Descending): ')
        if Input=='id':
            if Order=='Ascending':
                Id=matchdf.sort_values(by=['id'], ascending=True)
                print(Id)
            elif Order=='Descending':
                Id=matchdf.sort_values(by=['id'], ascending=False)
                print(Id)
        elif Input=='city':
            if Order=='Ascending':
                City=matchdf.sort_values(by=['city'], ascending=True)
                print(City)
            elif Order=='Descending':
                City=matchdf.sort_values(by=['city'], ascending=False)
                print(City)
        elif Input=='date':
            if Order=='Ascending':
                Date=matchdf.sort_values(by=['date'], ascending=True)
                print(Date)
            elif Order=='Descending':
                Date=matchdf.sort_values(by=['date'], ascending=False)
                print(Date)
        elif Input=='player_of_match':
            if Order=='Ascending':
                PlayerOfMatch=matchdf.sort_values(by=['player_of_match'], ascending=True)
                print(PlayerOfMatch)
            elif Order=='Descending':
                PlayerOfMatch=matchdf.sort_values(by=['player_of_match'], ascending=False)
                print(PlayerOfMatch)
        elif Input=='venue':
            if Order=='Ascending':
                Venue=matchdf.sort_values(by=['venue'], ascending=True)
                print(Venue)
            elif Order=='Descending':
                Venue=matchdf.sort_values(by=['venue'], ascending=False)
                print(Venue)
        elif Input=='neutral_venue':
            if Order=='Ascending':
                NeutralVenue=matchdf.sort_values(by=['neutral_venue'], ascending=True)
                print(NeutralVenue)
            elif Order=='Descending':
                NeutralVenue=matchdf.sort_values(by=['neutral_venue'], ascending=False)
                print(NeutralVenue)
        elif Input=='team1':
            if Order=='Ascending':
                Team=matchdf.sort_values(by=['team1'], ascending=True)
                print(Team)
            elif Order=='Descending':
                Team=matchdf.sort_values(by=['team1'], ascending=False)
                print(Team)
        elif Input=='team2':
            if Order=='Ascending':
                Team=matchdf.sort_values(by=['team2'], ascending=True)
                print(Team)
            elif Order=='Descending':
                Team=matchdf.sort_values(by=['team2'], ascending=False)
                print(Team)
        elif Input=='toss_winner':
            if Order=='Ascending':
                TossWinner=matchdf.sort_values(by=['toss_winner'], ascending=True)
                print(TossWinner)
            elif Order=='Descending':
                TossWinner=matchdf.sort_values(by=['toss_winner'], ascending=False)
                print(TossWinner)
        elif Input=='toss_decision':
            if Order=='Ascending':
                TossDecision=matchdf.sort_values(by=['toss_decision'], ascending=True)
                print(TossDecision)
            elif Order=='Descending':
                TossDecision=matchdf.sort_values(by=['toss_decision'], ascending=False)
                print(TossDecision)
        elif Input=='winner':
            if Order=='Ascending':
                Winner=matchdf.sort_values(by=['winner'], ascending=True)
                print(Winner)
            elif Order=='Descending':
                Winner=matchdf.sort_values(by=['winner'], ascending=False)
                print(Winner)
        elif Input=='result':
            if Order=='Ascending':
                Result=matchdf.sort_values(by=['result'], ascending=True)
                print(Result)
            elif Order=='Descending':
                Result=matchdf.sort_values(by=['result'], ascending=False)
                print(Result)
        elif Input=='result_margin':
            if Order=='Ascending':
                ResultMargin=matchdf.sort_values(by=['result_margin'], ascending=True)
                print(ResultMargin)
            elif Order=='Descending':
                ResultMargin=matchdf.sort_values(by=['result_margin'], ascending=False)
                print(ResultMargin)
        elif Input=='eliminator':
            if Order=='Ascending':
                Eliminator=matchdf.sort_values(by=['eliminator'], ascending=True)
                print(Eliminator)
            elif Order=='Descending':
                Eliminator=matchdf.sort_values(by=['eliminator'], ascending=False)
                print(Eliminator)
        elif Input=='method':
            if Order=='Ascending':
                Method=matchdf.sort_values(by=['method'], ascending=True)
                print(Method)
            elif Order=='Descending':
                Method=matchdf.sort_values(by=['method'], ascending=False)
                print(Method)
        elif Input=='umpire1':
            if Order=='Ascending':
                Umpire1=matchdf.sort_values(by=['umpire1'], ascending=True)
                print(Umpire1)
            elif Order=='Descending':
                Umpire1=matchdf.sort_values(by=['umpire1'], ascending=False)
                print(Umpire1)
        elif Input=='umpire2':
            if Order=='Ascending':
                Umpire2=matchdf.sort_values(by=['umpire2'], ascending=True)
                print(Umpire2)
            elif Order=='Descending':
                Umpire2=matchdf.sort_values(by=['umpire2'], ascending=False)
                print(Umpire2)
                
    Restart=input("Do you want to run the program again? (Yes/No)")
    if Restart=="Yes":
        main()
    else:
        exit()
main()
    

        
        






