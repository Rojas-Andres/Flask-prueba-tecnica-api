
class Query():
    def mascotas(self):
        query=""" 
            select * from mascotas;
        """
        return query
    def no_adoptadas(self):
        query="""
        select * from mascotas where propietario is null
        """ 
        return query 
    def cantidad_mascotas(self):
        query=""" 
            select
                count(*),
                tm.descripcion 
            from
                mascotas m
            inner join tipo_mascota tm on
                m.tipo_mascota = tm.idtipo_mascota
            group by
                tm.descripcion
        """ 
        return query 
    def propietarios_mascotas(self):
        query =""" 
            select
                p.nombre,
                count(*)
            from
                mascotas m
            inner join propietario p on
                m.propietario = p.idpropietario
            group by
                p.nombre
            having
                count(*)>1
        """ 
        return query
    def cant_mas_pro(self):
        query =""" 
            select
                p.nombre ,
                tm.descripcion ,
                count(*)
            from
                propietario p
            inner join mascotas m on
                p.idpropietario = m.propietario
            inner join tipo_mascota tm on
                m.tipo_mascota = tm.idtipo_mascota 
            group by 
            p.nombre,tm.descripcion 
            ;
        """ 
        return query 
    def propietario_no_mascota(self):
        query ="""              
            select
                p.nombre
            from
                propietario p
            except 
            select
                p.nombre
            from
                propietario p
            inner join mascotas m on
                p.idpropietario = m.propietario ;
        """ 
        return query 