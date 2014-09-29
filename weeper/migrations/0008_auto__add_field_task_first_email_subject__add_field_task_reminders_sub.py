# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Task.first_email_subject'
        db.add_column(u'weeper_task', 'first_email_subject',
                      self.gf('django.db.models.fields.CharField')(default=u'\xd0\x97\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb0', max_length=100),
                      keep_default=False)

        # Adding field 'Task.reminders_subject'
        db.add_column(u'weeper_task', 'reminders_subject',
                      self.gf('django.db.models.fields.CharField')(default=u'\xd0\x9d\xd0\xb0\xd0\xbf\xd0\xbe\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd0\xbd\xd0\xb8\xd0\xb5', max_length=100),
                      keep_default=False)

        # Adding field 'Task.day_before_deadline_subject'
        db.add_column(u'weeper_task', 'day_before_deadline_subject',
                      self.gf('django.db.models.fields.CharField')(default=u'\xd0\x9d\xd0\xb0\xd0\xbf\xd0\xbe\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', max_length=100),
                      keep_default=False)

        # Adding field 'Task.day_deadline_subject'
        db.add_column(u'weeper_task', 'day_deadline_subject',
                      self.gf('django.db.models.fields.CharField')(default=u'\xd0\x9d\xd0\xb0\xd0\xbf\xd0\xbe\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', max_length=100),
                      keep_default=False)

        # Adding field 'Task.after_deadline_subject'
        db.add_column(u'weeper_task', 'after_deadline_subject',
                      self.gf('django.db.models.fields.CharField')(default=u'\xd0\x9d\xd0\xb0\xd0\xbf\xd0\xbe\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', max_length=100),
                      keep_default=False)

        # Adding field 'Task.last_email_subject'
        db.add_column(u'weeper_task', 'last_email_subject',
                      self.gf('django.db.models.fields.CharField')(default=u'\xd0\x97\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb0 \xd0\xbd\xd0\xb5 \xd0\xb2\xd1\x8b\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb0', max_length=100),
                      keep_default=False)

        # Adding field 'TaskDelivery.first_email_subject'
        db.add_column(u'weeper_taskdelivery', 'first_email_subject',
                      self.gf('django.db.models.fields.CharField')(default=u'\u0417\u0430\u0434\u0430\u0447\u0430', max_length=100),
                      keep_default=False)

        # Adding field 'TaskDelivery.reminders_subject'
        db.add_column(u'weeper_taskdelivery', 'reminders_subject',
                      self.gf('django.db.models.fields.CharField')(default=u'\u041d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0435', max_length=100),
                      keep_default=False)

        # Adding field 'TaskDelivery.day_before_deadline_subject'
        db.add_column(u'weeper_taskdelivery', 'day_before_deadline_subject',
                      self.gf('django.db.models.fields.CharField')(default=u'\u041d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0435', max_length=100),
                      keep_default=False)

        # Adding field 'TaskDelivery.day_deadline_subject'
        db.add_column(u'weeper_taskdelivery', 'day_deadline_subject',
                      self.gf('django.db.models.fields.CharField')(default=u'\u041d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0435', max_length=100),
                      keep_default=False)

        # Adding field 'TaskDelivery.after_deadline_subject'
        db.add_column(u'weeper_taskdelivery', 'after_deadline_subject',
                      self.gf('django.db.models.fields.CharField')(default=u'\u041d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0435', max_length=100),
                      keep_default=False)

        # Adding field 'TaskDelivery.last_email_subject'
        db.add_column(u'weeper_taskdelivery', 'last_email_subject',
                      self.gf('django.db.models.fields.CharField')(default=u'\u0417\u0430\u0434\u0430\u0447\u0430 \u043d\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0430', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Task.first_email_subject'
        db.delete_column(u'weeper_task', 'first_email_subject')

        # Deleting field 'Task.reminders_subject'
        db.delete_column(u'weeper_task', 'reminders_subject')

        # Deleting field 'Task.day_before_deadline_subject'
        db.delete_column(u'weeper_task', 'day_before_deadline_subject')

        # Deleting field 'Task.day_deadline_subject'
        db.delete_column(u'weeper_task', 'day_deadline_subject')

        # Deleting field 'Task.after_deadline_subject'
        db.delete_column(u'weeper_task', 'after_deadline_subject')

        # Deleting field 'Task.last_email_subject'
        db.delete_column(u'weeper_task', 'last_email_subject')

        # Deleting field 'TaskDelivery.first_email_subject'
        db.delete_column(u'weeper_taskdelivery', 'first_email_subject')

        # Deleting field 'TaskDelivery.reminders_subject'
        db.delete_column(u'weeper_taskdelivery', 'reminders_subject')

        # Deleting field 'TaskDelivery.day_before_deadline_subject'
        db.delete_column(u'weeper_taskdelivery', 'day_before_deadline_subject')

        # Deleting field 'TaskDelivery.day_deadline_subject'
        db.delete_column(u'weeper_taskdelivery', 'day_deadline_subject')

        # Deleting field 'TaskDelivery.after_deadline_subject'
        db.delete_column(u'weeper_taskdelivery', 'after_deadline_subject')

        # Deleting field 'TaskDelivery.last_email_subject'
        db.delete_column(u'weeper_taskdelivery', 'last_email_subject')


    models = {
        u'action_user.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
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
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
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
        u'mailer.message': {
            'Meta': {'object_name': 'Message'},
            'from_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_body': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'2'", 'max_length': '1'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'to_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'when_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'weeper.task': {
            'Meta': {'unique_together': "(('task_delivery', 'user'),)", 'object_name': 'Task'},
            'after_deadline_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'after_deadline_text': ('django.db.models.fields.TextField', [], {}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_complete': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'day_before_deadline_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'day_before_deadline_text': ('django.db.models.fields.TextField', [], {}),
            'day_deadline_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'day_deadline_text': ('django.db.models.fields.TextField', [], {}),
            'first_email_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_email_text': ('django.db.models.fields.TextField', [], {}),
            'hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_email_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_email_text': ('django.db.models.fields.TextField', [], {}),
            'mails': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['mailer.Message']", 'null': 'True', 'blank': 'True'}),
            'reminders_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'reminders_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'reminders_text': ('django.db.models.fields.TextField', [], {}),
            'send_day_before_deadline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'send_day_deadline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'send_first_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'send_last_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'send_reminders': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'task_delivery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['weeper.TaskDelivery']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['action_user.User']"})
        },
        u'weeper.taskdelivery': {
            'Meta': {'object_name': 'TaskDelivery'},
            'after_deadline_subject': ('django.db.models.fields.CharField', [], {'default': "u'\\u041d\\u0430\\u043f\\u043e\\u043c\\u0438\\u043d\\u0430\\u043d\\u0438\\u0435'", 'max_length': '100'}),
            'after_deadline_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'close_tasks_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'complete_by_redirect': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_send': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'day_before_deadline_subject': ('django.db.models.fields.CharField', [], {'default': "u'\\u041d\\u0430\\u043f\\u043e\\u043c\\u0438\\u043d\\u0430\\u043d\\u0438\\u0435'", 'max_length': '100'}),
            'day_before_deadline_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'day_deadline_subject': ('django.db.models.fields.CharField', [], {'default': "u'\\u041d\\u0430\\u043f\\u043e\\u043c\\u0438\\u043d\\u0430\\u043d\\u0438\\u0435'", 'max_length': '100'}),
            'day_deadline_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {}),
            'first_email_subject': ('django.db.models.fields.CharField', [], {'default': "u'\\u0417\\u0430\\u0434\\u0430\\u0447\\u0430'", 'max_length': '100'}),
            'first_email_text': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_email_subject': ('django.db.models.fields.CharField', [], {'default': "u'\\u0417\\u0430\\u0434\\u0430\\u0447\\u0430 \\u043d\\u0435 \\u0432\\u044b\\u043f\\u043e\\u043b\\u043d\\u0435\\u043d\\u0430'", 'max_length': '100'}),
            'last_email_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'reminders_subject': ('django.db.models.fields.CharField', [], {'default': "u'\\u041d\\u0430\\u043f\\u043e\\u043c\\u0438\\u043d\\u0430\\u043d\\u0438\\u0435'", 'max_length': '100'}),
            'reminders_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'task_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['action_user.User']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['weeper']