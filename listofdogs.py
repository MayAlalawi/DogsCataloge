from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Dogs, Base, DogsItem, User

engine = create_engine('sqlite:///dogscatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="May Ali", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/' +
             '18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# list for Sporting Group
group1 = Dogs(user_id=1, name="Sporting Group")
session.add(group1)
session.commit()

# Brittany Dog
brittany_dog = DogsItem(user_id=1, name="Brittany",
                        group="Sporting Group",
                        height="17.5-20.5 inches",
                        weight="30-40 pounds",
                        temperament="Bright, Fun-Loving, Upbeat ",
                        description="Sportsmen on both sides of the Atlantic" +
                        "cherish the agile, energetic Brittany as a stylish " +
                        "and versatile gundog. Bright and eager at home," +
                        " and tireless afield, Brittanys require a lot " +
                        "of exercises, preferably with their favorite humans.",
                        dogs=group1)

session.add(brittany_dog)
session.commit()

# English Setter Dog
english_setter = DogsItem(
    user_id=1,
    name="English Setter",
    group="Sporting Group",
    height="25-27 inches",
    weight="65-80 pounds",
    temperament="Friendly, Mellow, Merry",
    description="The English Setter is a medium sized sporting dog " +
    "of sweet temper and show stopping good looks." +
    "It is one of the AKS's four British setters created to work on" +
    " the distinctly different terrains of England, Ireland, and Scotland.",
    dogs=group1
    )

session.add(english_setter)
session.commit()

# list for Hound Group
group2 = Dogs(user_id=1, name="Hound Group")
session.add(group2)
session.commit()

# Basenji Dog
basenji_dog = DogsItem(
    user_id=1,
    name="Basenji",
    group="Hound Group",
    height="17 inches",
    weight="24 pounds",
    temperament="Independent, Smart, Poised",
    description="The Basenji, Africa's Barkless Dog, is a compact, " +
    "sweet-faced hunter of intelligence and poise.They are unique and" +
    "beguiling pets, best for owners who can meet " +
    " their exercise needs and the challenge of training this catlike canine.",
    dogs=group2
    )

session.add(basenji_dog)
session.commit()

# Beagle Dog
beagle_dog = DogsItem(
    user_id=1,
    name="Beagle Dog",
    group="Hound Group",
    height="13 inches",
    weight="under 20 pounds",
    temperament="Friendly, Curious, Merry",
    description="Not only is the Beagle an excellent hunting dog and loyal " +
    "companion, it is also happy-go-lucky, funny, and cute.They were " +
    "bred to hunt in packs, so they enjoy company and are " +
    "generally easygoing.",
    dogs=group2)

session.add(beagle_dog)
session.commit()


# list for Working Group
group3 = Dogs(user_id=1, name="Working Group")
session.add(group3)
session.commit()

# Boerboel Dog
boerboel_dog = DogsItem(
    user_id=1,
    name="Boerboel",
    group="Working Group",
    height="24-27 inches",
    weight="150-200  pounds",
    temperament="Confident, Intelligent, Calm",
    description="Boerboels are intimidating but discerning guardians of " +
    "home and family who learned their trade while protecting " +
    "remote South African homesteads from ferocious predators." +
    "They are dominant and confident,also bright and eager to learn.",
    dogs=group3
    )

session.add(boerboel_dog)
session.commit()

# Akita Dog
akita_dog = DogsItem(
    user_id=1,
    name="Akita Dog",
    group="Working Group",
    height="26-28 inches",
    weight="100-130  pounds",
    temperament="Courageous, Dignified, Profoundly Loyal ",
    description="Akita is muscular, double-coated dogs of ancient " +
    "Japanese lineage famous for her dignity, courage, and loyalty." +
    "In her native land, she's venerated as family protectors and" +
    "symbols of good health, happiness, and long life.",
    dogs=group3
    )

session.add(akita_dog)
session.commit()


# list for Terrier Group
group4 = Dogs(user_id=1, name="Terrier Group")
session.add(group4)
session.commit()

# Australian Terrier
australian_terrier = DogsItem(
    user_id=1,
    name="Australian Terrier",
    group="Terrier Group",
    height="10-11 inches",
    weight="15-20 pounds",
    temperament="Affectionate, Courageous, Spirited",
    description="The diminutive Australian Terrier is plucky, spirited," +
    " and smart how did they fit so much dog into such a bitty package?  " +
    "Upbeat and lively, the self assured Aussie approaches life " +
    "with plenty of the old-time terrier curiosity and grit.",
    dogs=group4
    )

session.add(australian_terrier)
session.commit()

# Bull Terrier
bull_terrier = DogsItem(
    user_id=1,
    name="Bull Terrier",
    group="Terrier Group",
    height="21-22 inches",
    weight="50-70  pounds",
    temperament="Playful, Charming, Mischievous",
    description="Among the most comical and mischievous citizens of " +
    "dogdom, the Bull Terrier is playful and endearing, sometimes " +
    "stubborn, but always devoted.These unique eggheads are exuberant, " +
    "muscular companions who thrive on affection and exercise.",
    dogs=group4
    )

session.add(bull_terrier)
session.commit()


# list for Sporting Group
group5 = Dogs(user_id=1, name="Toy Group")
session.add(group5)
session.commit()

# list for Sporting Group
group6 = Dogs(user_id=1, name="Non-Sporting Group")
session.add(group6)
session.commit()

# list for Sporting Group
group7 = Dogs(user_id=1, name="Herding Group")
session.add(group7)
session.commit()
print "added group items!"
