#  A race event class definition for saving each instance of a race to a class.

# - Add in functionality to within the class.
# - Convert times to ms within here to simplify down the line?


""" Take all the data from the given .csv files and assign it to a class type. """
class RaceEvent:

    def __init__(self, Date, JetBet, Track, DayType, MeetingType, Club, MeetingName,
    TrackCondition,	TrackConditionScale, TrackWeather, Rail, RaceID, RaceNumber, RaceGroup,
    RaceType, Distance,	RaceClass, RaceName, Stake, Time, NoAllowances, MinWeight, ClassAge,	
    Class, ClassGender,	ClassWeight, RaceTrackCondition, RaceTrackConditionScale, RaceWeather,	
    HorseID, ToteNumber, Barrier, HorseName, Age, Gender, Weight, Finishingposition, Actualtime,	
    Last600mTime, Decimalmargin, Traditionalmargin, Trainer, TrainerLocation, StartingPriceWin,	
    StartingPricePlace, JockeyName, CarriedWeight, WeightDifference, DomesticRating, 
    HurdlesRating, SteeplesRating, GearWorn, SireID, Sire, DamID, Dam):
        self.Date = Date	
        self.JetBet	= JetBet
        self.Track = Track
        self.DayType = DayType
        self.MeetingType = MeetingType
        self.Club = Club	
        self.MeetingName = MeetingName	
        self.TrackCondition	= TrackCondition
        self.TrackConditionScale = TrackConditionScale	
        self.TrackWeather = MeetingName	
        self.Rail = Rail
        self.RaceID	= RaceID
        self.RaceNumber = RaceNumber 	
        self.RaceGroup = RaceGroup
        self.RaceType = RaceType
        self.Distance = Distance	
        self.RaceClass = RaceClass
        self.RaceName = RaceName
        self.Stake = Stake
        self.Time = Time
        self.NoAllowances = NoAllowances	
        self.MinWeight = MinWeight
        self.ClassAge = ClassAge	
        self.Class = Class
        self.ClassGender = ClassGender	
        self.ClassWeight = ClassWeight
        self.RaceTrackCondition	= RaceTrackCondition	
        self.RaceTrackConditionScale = RaceTrackConditionScale
        self.RaceWeather = RaceWeather	
        self.HorseID = HorseID
        self.ToteNumber	= ToteNumber
        self.Barrier = Barrier	
        self.HorseName = HorseName	
        self.Age = Age	
        self.Gender = Gender	
        self.Weight	= Weight
        self.Finishingposition = Finishingposition	
        self.Actualtime = Actualtime	
        self.Last600mTime = Last600mTime	
        self.Decimalmargin = Decimalmargin
        self.Traditionalmargin = Traditionalmargin
        self.Trainer = Trainer	
        self.TrainerLocation = TrainerLocation	
        self.StartingPriceWin = StartingPriceWin
        self.StartingPricePlace	= StartingPricePlace
        self.JockeyName	= JockeyName
        self.CarriedWeight = CarriedWeight	
        self.WeightDifference =	WeightDifference
        self.DomesticRating	= DomesticRating
        self.HurdlesRating = HurdlesRating	
        self.SteeplesRating	= SteeplesRating
        self.GearWorn = GearWorn	
        self.SireID	= SireID
        self.Sire = Sire
        self.DamID = DamID
        self.Dam = Dam
