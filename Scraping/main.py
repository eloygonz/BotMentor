from package.scraping import scraping
from package import crearTablasDB
from package import BBDD



def main():
	
	

########################-Tutorias-##############################################
	
	scrap = scraping.Scraping()

	dicCursos = scrap.scrapCursos()
	
	tabTutorias = scrap.scrapTutorias()
	
	tabAsignaturas = scrap.scrapAsignaturas()
	

	d = BBDD.DBHorarios();

	d.insertarScrapingBBDD(tabTutorias);

	d.insertarAsignaturas(tabAsignaturas);

	d.insertarCursos(dicCursos);
	d.selectCursos();



if __name__ == "__main__":
    main()