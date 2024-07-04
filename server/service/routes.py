# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from typing import Annotated, Literal, List, Any
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, BackgroundTasks, Query
from common import getConfig, Logger, MultiTask, AsyncRest
from .controls import Control
from common import ID, ModelStatus

from schema.sample.model import Blog, Message

#===============================================================================
# SingleTone
#===============================================================================
config = getConfig('../module.ini')
Logger.register(config)
api = FastAPI(title=config['default']['title'], separate_input_output_schemas=False)
ctrl = Control(api, config)


#===============================================================================
# API Interfaces
#===============================================================================
@api.get('/blog/count')
async def count_blog(filter:Annotated[str | None, Query(alias='$filter', description='lucene type filter ex) $filter=fieldName:yourSearchText')]=None):
    return await Blog.countModels(filter=filter)


@api.get('/blog/{id}')
async def read_blog(id:ID):
    return await Blog.readModelByID(id)


@api.get('/blog')
async def search_blog(filter:Annotated[str | None, Query(alias='$filter', description='lucene type filter ex) $filter=fieldName:yourSearchText')]=None):
    return await Blog.searchModels(filter=filter)


@api.post('/blog')
async def create_blog(blog:Blog):
    return await blog.createModel()


@api.put('/blog/{id}')
async def update_blog(id:ID, blog:Blog):
    blog.id = id
    return await blog.updateModel()


@api.delete('/blog/{id}')
async def delete_blog(id:ID):
    return await Blog.deleteModelByID(id)

