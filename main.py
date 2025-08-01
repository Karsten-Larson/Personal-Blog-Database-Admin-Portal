from model import engine, Content, Tag, ContentTag, Project, Post
from fastapi import FastAPI
from sqladmin import Admin, ModelView


app = FastAPI()
admin = Admin(app, engine)


class ContentAdmin(ModelView, model=Content):
    column_list = [
        Content.pk_content, 
        Content.title, 
        Content.slug, 
        Content.publication_date, 
        Content.image_url
    ]


class TagAdmin(ModelView, model=Tag):
    column_list = [Tag.pk_tag, Tag.name]


class ContentTagAdmin(ModelView, model=ContentTag):
    column_list = [ContentTag.content_id, ContentTag.tag_id]


class ProjectAdmin(ModelView, model=Project):
    column_list = [Project.pk_project, Project.content_id, Project.project_url, Project.source_url]


class PostAdmin(ModelView, model=Post):
    column_list = [Post.pk_post, Post.content_id, Post.project_id]

admin.add_view(PostAdmin)
admin.add_view(ProjectAdmin)
admin.add_view(ContentAdmin)
admin.add_view(TagAdmin)
admin.add_view(ContentTagAdmin)