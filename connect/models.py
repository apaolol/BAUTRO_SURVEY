from sqlmodel import Field , SQLModel


class Answers(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    ans1: str
    ans2: str
    ans3: str
    ans4: str
    ans5: str
    ans6: str
    ans7: str
    ans8: str
    ans9: str
    ans10: str





