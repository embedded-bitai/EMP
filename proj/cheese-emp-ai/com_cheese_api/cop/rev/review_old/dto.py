from com_cheese_api.ext.db import db

'''
userid password                                               name  pclass  gender age_group  embarked  rank
0         1        1                            Braund, Mr. Owen Harris       3       0         4         1     1
1         2        1  Cumings, Mrs. John Bradley (Florence Briggs Th...       1       1         6         2     3
2         3        1                             Heikkinen, Miss. Laina       3       1         5         1     2
3         4        1       Futrelle, Mrs. Jacques Heath (Lily May Peel)       1       1         5         1     3
4         5        1                           Allen, Mr. William Henry       3       0         5         1     1
..      ...      ...                                                ...     ...     ...       ...       ...   ...
886     887        1                              Montvila, Rev. Juozas       2       0         5         1     6
887     888        1                       Graham, Miss. Margaret Edith       1       1         4         1     2
888     889        1           Johnston, Miss. Catherine Helen "Carrie"       3       1         2         1     2
889     890        1                              Behr, Mr. Karl Howell       1       0         5         2     1
890     891        1                                Dooley, Mr. Patrick       3       0         5         3     1
[891 rows x 8 columns]
'''
class UserDto(db.Model):

    __tablename__ = 'users'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}

    userid: str = db.Column(db.String(10), primary_key = True, index = True)
    password: str = db.Column(db.String(1))
    name: str = db.Column(db.String(100))
    pclass: int = db.Column(db.Integer)
    gender: int = db.Column(db.Integer)
    age_group: int = db.Column(db.Integer)
    embarked: int = db.Column(db.Integer)
    rank: int = db.Column(db.Integer)

    def __init__(self, userid, password, name, pclass, gender, age_group, embarked, rank):
        self.userid = userid
        self.password = password
        self.name = name
        self.pclass = pclass
        self.gender = gender
        self.age_group = age_group
        self.embarked = embarked
        self.rank = rank

    def __repr__(self):
        return f'User(id={self.id}, userid={self.userid},\
            password={self.password}, name={self.name}, pclass={self.pclass}, gender={self.gender}, \
                age_group={self.age_group}, embarked={self.embarked}, rank={self.rank})'

    @property
    def json(self):
        return {
            'userid' : self.userid,
            'password' : self.password,
            'name' : self.name,
            'pclass' : self.pclass,
            'gender' : self.gender,
            'age_group' : self.age_group,
            'embarked' : self.embarked,
            'rank' : self.rank
        }

    
class UserVo:
    userid: str = ''
    password: str = ''
    name: str = ''
    pclass: int = 0
    gender: int = 0
    age_group: int = 0
    embarked: int = 0
    rank: int = 0