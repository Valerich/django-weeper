# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TaskDelivery'
        db.create_table(u'weeper_taskdelivery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('deadline', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_send', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('task_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('first_email_text', self.gf('django.db.models.fields.TextField')()),
            ('reminders_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('day_before_deadline_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('day_deadline_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('after_deadline_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'weeper', ['TaskDelivery'])

        # Adding M2M table for field users on 'TaskDelivery'
        db.create_table(u'weeper_taskdelivery_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('taskdelivery', models.ForeignKey(orm[u'weeper.taskdelivery'], null=False)),
            ('user', models.ForeignKey(orm[u'action_user.user'], null=False))
        ))
        db.create_unique(u'weeper_taskdelivery_users', ['taskdelivery_id', 'user_id'])

        # Adding model 'Task'
        db.create_table(u'weeper_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['action_user.User'])),
            ('date_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_complete', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_complete', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('hash', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('task_delivery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['weeper.TaskDelivery'])),
            ('deadline', self.gf('django.db.models.fields.DateTimeField')()),
            ('first_email_text', self.gf('django.db.models.fields.TextField')()),
            ('reminders_text', self.gf('django.db.models.fields.TextField')()),
            ('day_before_deadline_text', self.gf('django.db.models.fields.TextField')()),
            ('day_deadline_text', self.gf('django.db.models.fields.TextField')()),
            ('after_deadline_text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'weeper', ['Task'])


    def backwards(self, orm):
        # Deleting model 'TaskDelivery'
        db.delete_table(u'weeper_taskdelivery')

        # Removing M2M table for field users on 'TaskDelivery'
        db.delete_table('weeper_taskdelivery_users')

        # Deleting model 'Task'
        db.delete_table(u'weeper_task')


    models = {
        u'action_user.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'last_name_plural': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('snippets.models.fields.PhoneField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'weeper.task': {
            'Meta': {'object_name': 'Task'},
            'after_deadline_text': ('django.db.models.fields.TextField', [], {}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_complete': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'day_before_deadline_text': ('django.db.models.fields.TextField', [], {}),
            'day_deadline_text': ('django.db.models.fields.TextField', [], {}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {}),
            'first_email_text': ('django.db.models.fields.TextField', [], {}),
            'hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reminders_text': ('django.db.models.fields.TextField', [], {}),
            'task_delivery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['weeper.TaskDelivery']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['action_user.User']"})
        },
        u'weeper.taskdelivery': {
            'Meta': {'object_name': 'TaskDelivery'},
            'after_deadline_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_send': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'day_before_deadline_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'day_deadline_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {}),
            'first_email_text': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'reminders_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'task_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['action_user.User']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['weeper']