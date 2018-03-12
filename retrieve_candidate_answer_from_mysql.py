#coding:utf-8
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

def retieve_candidate_answer(topic_entity, answer_type):
    candidate_answer_list = []
    done = 0
    cn = MySQLdb.connect('localhost', 'jsd', '123456', 'BioKB_test')
    cur = cn.cursor()
    sql = ''
    for i in range(0, len(topic_entity)):
        topic_entity[i] = topic_entity[i].replace("'", "\\\'")
        if(answer_type == 'disease'):
            sql = "select efo_term from ch_temp_indication_new where drug_chembl_id in (select chembl_ID from synonyms_drug_integrated where synonym_name ='"+topic_entity[i]+"') union select diseaseName from disgenet_temp.gene_disease where geneSymbol ='"+topic_entity[i]+"'"
        elif(answer_type == 'target'):
                sql = "select target_name from target_drug_integrated where chembl_ID in (select chembl_ID from synonyms_drug_integrated where synonym_name = '"+topic_entity[i]+"' and chembl_ID != 'NULL')"
        elif(answer_type=='drug'):
            sql = "select synonym_name from synonyms_drug_integrated where chembl_ID in (select drug_chembl_id from ch_temp_indication_new where efo_term = '"+topic_entity[i]+"')"
        elif(answer_type == 'gene'):
            sql = "select geneSymbol from disgenet_temp.gene_disease where diseaseName = '"+topic_entity[i]+"'"
        else:
            sql = "select efo_term from ch_temp_indication_new where drug_chembl_id in (select chembl_ID from synonyms_drug_integrated where synonym_name ='Orteronel')"
        #sql_safe = MySQLdb.escape_string(sql)
        #sql = sql.replace("'","\\\'")
        print(sql)
        cur.execute(sql)##sql_safe
        #cur.execute(sql_safe)
        results = cur.fetchall()
        for row in results:
            if(row[0]!='NULL' and row[0]!='IsNULL' and row[0] not in candidate_answer_list ):
                candidate_answer_list.append(row[0])




    cur.close()
    cn.commit()
    cn.close()
    return candidate_answer_list



