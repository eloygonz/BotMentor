from package.scraping import scraping
from package import crearTablasDB
from package import BBDD



def main():
	
	

########################-Tutorias-##############################################
	
	scrap = scraping.Scraping()

	
	tabTutorias = scrap.scrapTutorias()
	
	tabAsignaturas = scrap.scrapAsignaturas()

	dicCursos = scrap.scrapCursos()
	
	dicFichas=scrap.scrapInformacionDocente()
	
	
	d = BBDD.DBHorarios();

	d.insertarScrapingBBDD(tabTutorias);

	d.insertarAsignaturas(tabAsignaturas);

	d.insertarCursos(dicCursos);
	
	d.insertarFichasDocentes(dicFichas)




if __name__ == "__main__":
    main()