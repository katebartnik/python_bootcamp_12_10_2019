import json
import logging
import os
import magic

from celery.signals import task_prerun, task_failure, task_success, task_postrun
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.indexes import GinIndex
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Max
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django_celery_results.models import TaskResult as TaskResultOrig
from elasticsearch_dsl.connections import Connections
from mimeparse import parse_mime_type
from model_utils import FieldTracker
from model_utils.managers import SoftDeletableManager
from modeltrans.fields import TranslationFieldfrom mcod.core import signals as core_signals

from mcod.core import storages
from mcod.core.api.search import signals as search_signals
from mcod.core.db.managers import DeletedManager
from mcod.core.db.models import ExtendedModel, update_watcher
from mcod.core.utils import sizeof_fmt
from mcod.datasets.models import Dataset
from mcod.lib.data_rules import painless_body
from mcod.resources.error_mappings import recommendations, messages
from mcod.resources.indexed_data import GeoData, TabularData
from mcod.resources.link_validation import content_type_from_file_format
from mcod.resources.signals import revalidate_resource
from mcod.resources.tasks import process_resource_from_url_task, process_resource_file_task, \
   process_resource_file_data_task
from mcod.watchers.tasks import update_model_watcher_task













import matematyka
import sys

print(sys.path)

print(matematyka.pole_kwadratu(2))

print(r"\nowe")

from matematyka import pole_kwadratu, pole_kola, FI, operatory
print(pole_kwadratu(2))

from matematyka import *
from algebra import *

from matematyka import dodaj_macierze as dodawanie1
from algebra import dodaj_macierze as dodawanie2

print(dodawanie1([[1, 2]], [[3, 4]]))
print(dodawanie2([[1, 2]], [[3, 4]]))
