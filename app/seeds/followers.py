from app.models import db, User, environment

def seed_followers():
    demo = User.query.get(1)
    jamie = User.query.get(2)
    jordan = User.query.get(3)
    nick = User.query.get(4)
    maria = User.query.get(5)
    shaina = User.query.get(6)
    brennen = User.query.get(7)
    andrew = User.query.get(8)
    sara = User.query.get(9)
    alex = User.query.get(10)
    katharine = User.query.get(11)
    marty = User.query.get(12)
    leslie = User.query.get(13)
    matt = User.query.get(14)
    gray = User.query.get(15)
    mike = User.query.get(16)
    jacob = User.query.get(17)
    tyler = User.query.get(18)
    chris= User.query.get(19)
    huishi = User.query.get(20)
    kevin = User.query.get(21)
    kat = User.query.get(22)
    ricardo = User.query.get(23)
    brian = User.query.get(24)
    dave = User.query.get(25)
    douglas = User.query.get(26)
    efrain = User.query.get(27)
    joonil = User.query.get(28)
    linus = User.query.get(29)
    michael = User.query.get(30)
    preston = User.query.get(31)
    trevor = User.query.get(32)
    riley = User.query.get(33)
    hannah = User.query.get(34)

    demo.followed.extend([shaina, brennen, andrew, sara, tyler, mike, chris, huishi, kevin, ricardo, kat, efrain, joonil, riley, hannah])
    jordan.followed.extend([nick, andrew, alex, jamie, demo, chris, katharine, riley, hannah])
    jamie.followed.extend([nick, alex, maria, jordan, demo, katharine, marty, leslie, shaina, demo, brennen, chris, riley, hannah])
    nick.followed.extend([jamie, jordan, alex, maria, shaina, andrew, marty, demo, leslie, chris, riley, hannah])
    maria.followed.extend([nick, alex, jamie, shaina, katharine, chris, riley, hannah])
    shaina.followed.extend([nick, alex, jamie, jordan, maria, andrew, katharine, chris, riley, hannah])
    brennen.followed.extend([jamie, chris])
    andrew.followed.extend([jordan, nick, alex, shaina, jamie, katharine, chris, riley, hannah])
    sara.followed.extend([matt, gray, mike, jacob, tyler, demo, chris, huishi, kevin, kat, ricardo, brian, dave, douglas, efrain, joonil, linus, michael, preston])
    alex.followed.extend([nick, jordan, maria, marty, leslie, shaina, jamie, andrew, chris, riley, hannah])
    katharine.followed.extend([nick, alex, jamie, shaina, maria, marty, leslie, jordan, andrew, chris, riley, hannah])
    marty.followed.extend([leslie, nick, alex, jamie, shaina, chris])
    leslie.followed.extend([marty, nick, alex, jamie, shaina, chris])
    matt.followed.extend([sara, gray, mike, jacob, tyler, demo, chris, huishi, kevin, kat, ricardo, brian, dave, douglas, efrain, joonil, linus, michael, preston, trevor])
    gray.followed.extend([sara, matt, mike, jacob, tyler, demo, chris, huishi, kevin, kat, ricardo, brian, dave, douglas, efrain, joonil, linus, michael, preston, trevor])
    mike.followed.extend([sara, matt, gray, jacob, tyler, demo, chris, huishi, kevin, kat, ricardo, brian, dave, douglas, efrain, joonil, linus, michael, preston, trevor])
    jacob.followed.extend([sara, matt, gray, mike, tyler, demo, chris, huishi, kevin, kat, ricardo, brian, dave, douglas, efrain, joonil, linus, michael, preston, trevor])
    tyler.followed.extend([sara, matt, gray, mike, jacob, demo, chris, huishi, kevin, kat, ricardo, brian, dave, douglas, efrain, joonil, linus, michael, preston, trevor])
    huishi.followed.extend([sara, matt, gray, mike, jacob, demo, chris, kevin, kat, ricardo, brian, dave, douglas, efrain, joonil, linus, michael, preston, trevor])
    kevin.followed.extend([sara, matt, gray, mike, jacob, demo, chris, huishi, kat, ricardo, brian, dave, douglas, efrain, joonil, linus, michael, preston, trevor])
    kat.followed.extend([sara, matt, gray, mike, jacob, demo, chris, huishi, kevin, ricardo, brian, dave, douglas, efrain, joonil, linus, michael, preston, trevor])
    ricardo.followed.extend([sara, matt, gray, mike, jacob, demo, chris, huishi, kevin, kat, brian, dave, douglas, efrain, joonil, linus, michael, preston, trevor])
    brian.followed.extend([sara, matt, gray, mike, jacob, demo, chris, huishi, kevin, kat, ricardo, dave, douglas, efrain, joonil, linus, michael, preston, trevor])
    dave.followed.extend([sara, matt, gray, mike, jacob, demo, chris, huishi, kevin, kat, ricardo, brian, douglas, efrain, joonil, linus, michael, preston, trevor])
    douglas.followed.extend([sara, matt, gray, mike, jacob, demo, chris, huishi, kevin, kat, ricardo, brian, dave, efrain, joonil, linus, michael, preston, trevor])
    efrain.followed.extend([sara, matt, gray, mike, jacob, demo, chris, huishi, kevin, kat, ricardo, brian, dave, douglas, joonil, linus, michael, preston, trevor])
    joonil.followed.extend([sara, matt, gray, mike, jacob, demo, chris, huishi, kevin, kat, ricardo, brian, dave, douglas, efrain, linus, michael, preston, trevor])
    linus.followed.extend([sara, matt, gray, mike, jacob, demo, chris, huishi, kevin, kat, ricardo, brian, dave, douglas, efrain, joonil, michael, preston, trevor])
    michael.followed.extend([sara, matt, gray, mike, jacob, demo, chris, huishi, kevin, kat, ricardo, brian, dave, douglas, efrain, joonil, linus, preston, trevor])
    preston.followed.extend([sara, matt, gray, mike, jacob, demo, chris, huishi, kevin, kat, ricardo, brian, dave, douglas, efrain, joonil, linus, michael, trevor])
    trevor.followed.extend([sara, matt, gray, mike, jacob, demo, chris, huishi, kevin, kat, ricardo, brian, dave, douglas, efrain, joonil, linus, michael, preston])
    chris.followed.extend([jamie, maria, shaina, brennen, andrew, nick, alex, demo, jordan, katharine, marty, leslie, sara, matt, gray, mike, jacob, demo, huishi, kevin, kat, ricardo, brian, dave, douglas, efrain, joonil, linus, michael, preston])
    riley.followed.extend([jordan, nick, andrew, alex, jamie, demo, chris, katharine, hannah])
    hannah.followed.extend([jordan, nick, andrew, alex, jamie, demo, chris, katharine, riley])

    db.session.commit()

def undo_followers():
    if environment == "production":
        db.session.execute(f"TRUNCATE table followers RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM followers")
        db.session.commit()
