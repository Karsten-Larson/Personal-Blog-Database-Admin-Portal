from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint, Text, String, create_engine
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL
)

# SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Content(Base):
    __tablename__ = "content"

    pk_content = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    content = Column(Text, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    publication_date = Column(String, nullable=False)
    image_url = Column(String)

    def __str__(self):
        return f"<Content(content_id={self.pk_content}, title='{self.title}', slug='{self.slug}')>"


class Tag(Base):
    __tablename__ = "tag"

    pk_tag = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __str__(self):
        return f"<Tag(tag_id={self.pk_tag}, name={self.name})>"


class ContentTag(Base):
    __tablename__ = "content_tags"

    content_id = Column(Integer, ForeignKey("content.pk_content"), nullable=False)
    tag_id = Column(Integer, ForeignKey("tag.pk_tag"), nullable=False)

    content = relationship("Content", backref=backref("content_tags", lazy="select"))
    tag = relationship("Tag", backref=backref("content_tags", lazy="select"))

    __table_args__ = (
        PrimaryKeyConstraint('content_id', 'tag_id'),
    )

    def __str__(self):
        return f"<ContentTag(content_id={self.content_id}, tag_id={self.tag_id})>"


class Project(Base):
    __tablename__ = "project"

    pk_project = Column(Integer, primary_key=True)
    content_id = Column(Integer, ForeignKey("content.pk_content"), nullable=False)
    project_url = Column(String, nullable=True)
    source_url = Column(String, nullable=True)

    content = relationship("Content", backref=backref("projects", lazy="select"))

    def __str__(self):
        return f"<Project(pk_project={self.pk_project}, content_id={self.content_id}, project_url='{self.project_url}')>"


class Post(Base):
    __tablename__ = "post"

    pk_post = Column(Integer, primary_key=True)

    content_id = Column(Integer, ForeignKey("content.pk_content"), nullable=False)
    project_id = Column(Integer, ForeignKey("project.pk_project"), nullable=True)

    content = relationship("Content", backref=backref("posts", lazy="select"))
    project = relationship("Project", backref=backref("posts", lazy="select"))

    def __str__(self):
        return f"<Post(pk_post={self.pk_post}, content_id={self.content_id}, project_id={self.project_id})>"


Base.metadata.create_all(bind=engine) # Ensure the database and tables are created