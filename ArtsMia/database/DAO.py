from database.DB_connect import DBConnect
from model.artista import Artista


class DAO():

    @staticmethod
    def getAllRoles():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct a.`role` 
                from authorship a
                order by a.`role`"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(row["role"])
            # result.append(ArtObject(object_id=row["object_id"], ... ))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getVertici(ruolo):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a.*
                from artists a, authorship a2 
                where a.artist_id = a2.artist_id and a2.`role` = %s 
                """

        cursor.execute(query, (ruolo,))

        for row in cursor:
            result.append(Artista(**row))


        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(uID,vID):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select  count(distinct (eo2.exhibition_id))as peso
                from authorship a, authorship a2, exhibition_objects eo, exhibition_objects eo2 
                where a.artist_id = %s and a2.artist_id = %s and a.object_id = eo.object_id and a2.object_id = eo2.object_id and eo2.exhibition_id = eo.exhibition_id
                """

        cursor.execute(query,(uID,vID,))

        for row in cursor:
            result.append(row["peso"])

        cursor.close()
        conn.close()
        return result