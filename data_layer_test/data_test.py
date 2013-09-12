#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011, Torbjörn Lönnemark <tobbez@ryara.net>
# Copyright (C) 2011, IDA, Linköping University
import unittest
import data
import hashlib
import sys
md5 = hashlib.md5
class DataTest(unittest.TestCase):
    def setUp(self):
        self.expected_data = [{u'big_image': u'XXX', u'project_name': u'python data-module test script', u'course_name': u'OK\xc4NT', u'group_size': 2, u'end_date': u'2009-09-06', u'techniques_used': [u'python'], u'academic_credits': u'WUT?', u'small_image': u'X', u'long_description': u'no no no', u'course_id': u'TDP003', u'project_no': 1, u'external_link': u'YY', u'short_description': u'no', u'start_date': u'2009-09-05', u'lulz_had': u'many'}, {u'big_image': u'XXX', u'project_name': u'NEJ', u'course_name': u'OK\xc4NT', u'group_size': 4, u'end_date': u'2009-09-08', u'techniques_used': [u'c++', u'csv', u'python'], u'academic_credits': u'WUT?', u'small_image': u'X', u'long_description': u'no no no', u'course_id': u'TDP003', u'project_no': 3, u'external_link': u'YY', u'short_description': u'no', u'start_date': u'2009-09-07', u'lulz_had': u'few'}, {u'big_image': u'XXX', u'project_name': u'2007', u'course_name': u'OK\xc4NT', u'group_size': 6, u'end_date': u'2009-09-09', u'techniques_used': [u'ada', u'python'], u'academic_credits': u'WUT?', u'small_image': u'X', u'long_description': u'no no no', u'course_id': u'TDP003', u'project_no': 2, u'external_link': u'YY', u'short_description': u'no', u'start_date': u'2009-09-08', u'lulz_had': u'medium'}, {u'big_image': u'XXX', u'project_name': u',', u'course_name': u'HOHO', u'group_size': 8, u'end_date': u'2009-09-07', u'techniques_used': [], u'academic_credits': u'WUT?', u'small_image': u'X', u'long_description': u'no no no', u'course_id': u' "', u'project_no': 4, u'external_link': u'YY', u'short_description': u'no', u'start_date': u'2009-09-06', u'lulz_had': u'over 9000'}]
        self.expected_technique_data = [u'ada', u'c++', u'csv', u'python']
        self.expected_technique_stat_data = {u'python': [{u'id': 2, u'name': u'2007'}, {u'id': 3, u'name': u'NEJ'}, {u'id': 1, u'name': u'python data-module test script'}], u'csv': [{u'id': 3, u'name': u'NEJ'}], u'c++': [{u'id': 3, u'name': u'NEJ'}], u'ada': [{u'id': 2, u'name': u'2007'}]}

        self.loaded_data = data.load("data.json")

    def test_load(self):
        self.assertEqual(self.loaded_data, self.expected_data)
        self.assertEqual(data.load("/dev/this_file_does_not_exist"), None)

    def test_get_project_count(self):
        self.assertEqual(data.get_project_count(self.loaded_data), 4)
        
    def test_get_project(self):
        self.assertEqual(data.get_project(self.loaded_data, 1)[u'project_no'], 1)
        self.assertEqual(data.get_project(self.loaded_data, 2)[u'project_no'], 2)
        self.assertEqual(data.get_project(self.loaded_data, 3)[u'project_no'], 3)
        self.assertEqual(data.get_project(self.loaded_data, 4)[u'project_no'], 4)
        self.assertEqual(data.get_project(self.loaded_data, 42), None)

    def test_search(self):
        self.assertEqual(len(data.search(self.loaded_data)), 4)

        self.assertEqual(len(data.search(self.loaded_data, techniques=[u'csv'])), 1)

        res = data.search(self.loaded_data, sort_order='asc',techniques=["python"])
        self.assertEqual(res[0][u'project_no'], 1)
        self.assertEqual(res[1][u'project_no'], 3)
        self.assertEqual(res[2][u'project_no'], 2)


        res = data.search(self.loaded_data, 
                                     sort_by="end_date", 
                                     search='okänt', 
                                     search_fields=['project_no','project_name','course_name'])
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0][u'project_no'], 2)
        self.assertEqual(res[1][u'project_no'], 3)
        self.assertEqual(res[2][u'project_no'], 1)
        
        res = data.search(self.loaded_data, 
                                     search="okänt", 
                                     search_fields=["project_no","project_name","course_name"])
        self.assertEqual(len(res), 3)

        res = data.search(self.loaded_data,
                                     techniques=[],
                                     search="okänt",
                                     search_fields=["project_no","project_name","course_name"])
        self.assertEqual(len(res), 3)

        res = data.search(self.loaded_data, search="okänt", search_fields=[])
        self.assertEqual(len(res), 0)

        res = data.search(self.loaded_data, sort_by='group_size')
        self.assertEqual(res[0][u'project_no'], 4)
        self.assertEqual(res[1][u'project_no'], 2)
        self.assertEqual(res[2][u'project_no'], 3)
        self.assertEqual(res[3][u'project_no'], 1)

    def test_get_techniques(self):
        res = data.get_techniques(self.loaded_data)
        self.assertEqual(res, self.expected_technique_data)

    def test_get_technique_stats(self):
        res = data.get_technique_stats(self.loaded_data)
        self.assertEqual(res, self.expected_technique_stat_data)


if __name__ == '__main__':
    print ("Test:     ", md5(sys.argv[0].encode('UTF-8')).hexdigest())
    print ("Test data:", md5(b"data.json").hexdigest())
    print
    unittest.main()
