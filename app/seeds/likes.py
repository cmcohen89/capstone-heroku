from app.models import db, Post, User, environment

def seed_likes():
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
    chris = User.query.get(19)
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

    post1 = Post.query.get(1)
    post2 = Post.query.get(2)
    post3 = Post.query.get(3)
    post4 = Post.query.get(4)
    post5 = Post.query.get(5)
    post6 = Post.query.get(6)
    post7 = Post.query.get(7)
    post8 = Post.query.get(8)
    post9 = Post.query.get(9)
    post10 = Post.query.get(10)
    post11 = Post.query.get(11)
    post12 = Post.query.get(12)
    post13 = Post.query.get(13)
    post14 = Post.query.get(14)
    post15 = Post.query.get(15)
    post16 = Post.query.get(16)
    post17 = Post.query.get(17)
    post18 = Post.query.get(18)
    post19 = Post.query.get(19)
    post20 = Post.query.get(20)
    post21 = Post.query.get(21)
    post22 = Post.query.get(22)
    post23 = Post.query.get(23)
    post24 = Post.query.get(24)
    post25 = Post.query.get(25)
    post26 = Post.query.get(26)
    post27 = Post.query.get(27)
    post28 = Post.query.get(28)
    post29 = Post.query.get(29)
    post30 = Post.query.get(30)
    post31 = Post.query.get(31)
    post32 = Post.query.get(32)
    post33 = Post.query.get(33)
    post34 = Post.query.get(34)
    post35 = Post.query.get(35)
    post36 = Post.query.get(36)
    post37 = Post.query.get(37)
    post38 = Post.query.get(38)

    demo.user_likes.extend([post1, post7, post10, post13, post14, post19, post20, post21])
    jamie.user_likes.extend([post1, post2, post4, post10, post11, post12, post13, post14, post19, post20, post21])
    jordan.user_likes.extend([post1, post2, post4, post6, post11, post12, post13, post14, post19, post20, post21])
    nick.user_likes.extend([post1, post2, post5, post6, post8, post11, post14, post19, post20, post21])
    maria.user_likes.extend([post4, post7, post11, post12, post13, post14])
    shaina.user_likes.extend([post3, post6, post9, post10, post22, post23, post24, post15, post16, post17, post18])
    brennen.user_likes.extend([post2, post3, post4, post5, post6])
    andrew.user_likes.extend([post7, post4, post8, post9, post10, post22, post23, post24, post15, post16, post17, post18, post11, post13, post14])
    sara.user_likes.extend([post1, post5, post6])
    alex.user_likes.extend([post1, post2, post3, post6, post9])
    katharine.user_likes.extend([post1, post2, post4])
    marty.user_likes.extend([post2, post3, post6])
    leslie.user_likes.extend([post7, post11])
    matt.user_likes.extend([post7, post8, post9, post10, post22, post23, post24, post15, post17, post18, post11])
    gray.user_likes.extend([post10, post15, post16, post17, post18, post11])
    mike.user_likes.extend([post7, post8])
    jacob.user_likes.extend([post1, post3, post4, post34, post35, post36, post37, post6, post9])
    tyler.user_likes.extend([post7, post3, post10, post4, post34, post35, post36, post37, post15, post16, post17, post18, post11, post1, post9])
    chris.user_likes.extend([post6, post3, post10, post4, post34, post35, post36, post37, post15, post18, post13, post1])
    huishi.user_likes.extend([post6, post3, post10, post4, post34, post35, post36, post15, post18, post13, post1])
    kevin.user_likes.extend([post6, post3, post10, post4, post15, post18, post13, post1])
    kat.user_likes.extend([post6, post3, post10, post4, post15, post18, post13, post1])
    ricardo.user_likes.extend([post3, post10, post4, post15, post25, post26, post27, post16, post17, post12, post13, post1])
    brian.user_likes.extend([post4, post10, post15, post25, post26, post27, post16, post17, post12, post13, post1])
    dave.user_likes.extend([post4, post10, post15, post25, post26, post27, post16, post17, post12, post13, post1])
    douglas.user_likes.extend([post4, post10, post15, post25, post26, post27, post16, post17, post12, post13, post1])
    efrain.user_likes.extend([post4, post10, post15, post25, post26, post38, post27, post16, post17, post12, post13, post1])
    joonil.user_likes.extend([post4, post10, post15, post25, post26, post38, post27, post16, post17, post12, post13, post1, post9])
    linus.user_likes.extend([post7, post4, post10, post5, post15, post16, post17, post12, post13, post1, post9])
    michael.user_likes.extend([post7, post4, post10, post5, post28, post29, post30, post31, post32, post33, post15, post16, post18, post11, post1, post9])
    preston.user_likes.extend([post7, post3, post10, post5, post28, post29, post30, post31, post32, post33, post15, post16, post18, post11, post1, post9])
    trevor.user_likes.extend([post7, post3, post10, post4, post15, post16, post18, post11, post1, post9])
    riley.user_likes.extend([post7, post3, post10, post4, post15, post16, post18, post11, post1, post9])
    hannah.user_likes.extend([post7, post3, post10, post4, post15, post16, post18, post11, post1, post9])

    db.session.commit()

def undo_likes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table likes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM likes")
        db.session.commit()
