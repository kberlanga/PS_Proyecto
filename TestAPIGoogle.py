import unittest
from APIConnectionGoogle import APIConnection, localBook, APIServiceExtra
from unittest.mock import patch
import requests
from interface_book import Book

class MockTest(unittest.TestCase):
    """Pruebas unitaria de la Google Books API"""

    @patch('requests.get')
    def test_mock(self, mock_get):
        # casos de prueba
        test_cases = (
        ("el principito", 200, '{"totalItems": 314, "items": [{ "volumeInfo": { "title": "El Principito / The Little Prince", "subtitle": "a", "authors": ["Antoine de Saint-Exupéry"], "publisher": "SELECTOR", "publishedDate": "2004-12-30", "description": "The little prince is the marvellous story of a small boy who comes from a planet barely larger than a house, and who asks questions and seeks answers to things that for adults might be of little importance.", "industryIdentifiers": [{"type": "ISBN_10", "identifier": "9706433910"}], "pageCount": 77, "categories": ["Juvenile Fiction"], "imageLinks": {"smallThumbnail": "http://books.google.com/books/content?id=CpvT1p6LHnoC&printsec=frontcover&img=1&zoom=5&source=gbs_api", "thumbnail": "http://books.google.com/books/content?id=CpvT1p6LHnoC&printsec=frontcover&img=1&zoom=1&source=gbs_api"}, "previewLink": "http://books.google.com.mx/books?id=CpvT1p6LHnoC&dq=El+principito+/+the+little+prince&hl=&cd=1&source=gbs_api"}, "accessInfo": {"pdf": {"isAvailable": False}}}]}' ,
        {"totalItems": 314, "items": [{"volumeInfo": {"title": "El Principito / The Little Prince", "subtitle": "a", "authors": ["Antoine de Saint-Exupéry"], "publisher": "SELECTOR", "publishedDate": "2004-12-30", "description":
        "The little prince is the marvellous story of a small boy who comes from a planet barely larger than a house, and who asks questions and seeks answers to things that for adults might be of little importance.",
        "industryIdentifiers": [{"type": "ISBN_10", "identifier": "9706433910"}], "pageCount": 77, "categories": ["Juvenile Fiction"], "imageLinks": {"smallThumbnail":
        "http://books.google.com/books/content?id=CpvT1p6LHnoC&printsec=frontcover&img=1&zoom=5&source=gbs_api", "thumbnail": "http://books.google.com/books/content?id=CpvT1p6LHnoC&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        },"previewLink": "http://books.google.com.mx/books?id=CpvT1p6LHnoC&dq=El+principito+/+the+little+prince&hl=&cd=1&source=gbs_api"}, "accessInfo": {"pdf": {"isAvailable": False}}}]},
        [Book("El Principito / The Little Prince", "a", ["Antoine de Saint-Exupéry"], "SELECTOR", "2004-12-30",
        "The little prince is the marvellous story of a small boy who comes from a planet barely larger than a house, and who asks questions and seeks answers to things that for adults might be of little importance.", "9706433910",
        77, ["Juvenile Fiction"], "http://books.google.com/books/content?id=CpvT1p6LHnoC&printsec=frontcover&img=1&zoom=1&source=gbs_api",
        "http://books.google.com.mx/books?id=CpvT1p6LHnoC&dq=El+principito+/+the+little+prince&hl=&cd=1&source=gbs_api", False, "no identificado")]),

        ("el principito", 404, '404 page not found', "", "LA SOLICITUD NO SE EJECUTÓ DE MANERA CORRECTA"),

        ("el principito", 500, '500 internal server error', "", "LA SOLICITUD NO SE EJECUTÓ DE MANERA CORRECTA"),

        ("fdshjoaowl", 200, '{"kind": "books#volumes", "totalItems": 0}', {"kind": "books#volumes", "totalItems": 0}, None),

        ("", 400, '', '', "LA SOLICITUD NO SE EJECUTÓ DE MANERA CORRECTA"))

        for entrada, stat, mock_text, mock_json, esperado in test_cases:
            mock_get.return_value.status_code = stat # creamos mock del status
            mock_get.return_value.json = lambda : mock_json # creamos un mock de la salida esperada
            salida_real = APIConnection().getBook(entrada, APIServiceExtra())
            # comparamos salida real con esperada
            self.assertEqual(salida_real, esperado)

    def testGetBook(self):
        """Test de los libros"""
        # salidas esperadas de la función getBook
        salida_esperadas = (("GOT", [
        Book("I Got This", "How I Changed My Ways and Lost What Weighed Me Down",['Jennifer Hudson'],"Penguin",'2012','''Relates the story of the author's meteoric rise from "American Idol" to "Dreamgirls" to her weight loss where she embraced a healthy lifestyle and lost more than eighty pounds.''','9780451239129',256,['Biography & Autobiography'],'http://books.google.com/books/content?id=HlooDgAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api',
        'http://books.google.com/books?id=HlooDgAAQBAJ&printsec=frontcover&dq=GOT&hl=&cd=1&source=gbs_api',False,'HA OCURRIDO UN ERROR'),
        Book('Have I Got a Book for You!','',['Mélanie Watt'],'Kids Can Press Ltd','2009',"Mr. Al Foxwood is an avid salesman and gives very persuasive reasons why someone should buy the book he is selling.",'9781554532896',32,['Juvenile Fiction'],'http://books.google.com/books/content?id=0XTom7UHUJcC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api',
        'http://books.google.com/books?id=0XTom7UHUJcC&printsec=frontcover&dq=GOT&hl=&cd=2&source=gbs_api',False,'no identificado'),
        Book("I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '1995', 'Traces the history of the civil rights movement in Mississippi, and describes how ordinary men and women became caught up in the struggle', '0520207068', 525, ['History'],
        'http://books.google.com/books/content?id=t0SdXs_dbk8C&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com/books?id=t0SdXs_dbk8C&printsec=frontcover&dq=GOT&hl=&cd=3&source=gbs_api', False ,'no identificado'),
        Book('Goom Got Game!','',['Jeff Parker'],'ABDO','2006-09-01',"Spider-Man takes on the monstrous Street, while the Fantastic Four's Human Torch needs his help to combat a slang-talking alien named Goom that he accidentally brought to Earth.","1599612097",24,['Juvenile Fiction'],'http://books.google.com/books/content?id=Bcfuuve7K30C&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api',
        'http://books.google.com/books?id=Bcfuuve7K30C&printsec=frontcover&dq=GOT&hl=&cd=5&source=gbs_api',False,'5.6 ounces'),
        Book('Got Game','How the Gamer Generation is Reshaping Business Forever',['John C. Beck'],'Harvard Business Press','2004',"Got Game shows how growing up immersed in video games has profoundly shaped the attitudes and abilities of this new generationThough little-noticed, these ninety million rising professionals, through sheer numbers, will inevitably dominate business-and are already changing the rules.While many of these changes are positive-such as more open communication and creative problem-solving-they have caused a generation gap that frustrates gamers and the boomers who manage them.Got Game identifies the distinct values and traits that define the gamer generation-from an increased appetite for risk to unexpected leadership skills-and reveals management techniques today's leaders can use to bridge the generation gap and unleash gamers' hidden potential.",'1578519497',202,['Business & Economics'],
        'http://books.google.com/books/content?id=uxz6UU_AW3cC&printsec=frontcover&img=1&zoom=1&source=gbs_api','http://books.google.com/books?id=uxz6UU_AW3cC&dq=GOT&hl=&cd=6&source=gbs_api',True,'1.1 pounds'),
        Book('Explorers Who Got Lost','',['Diane Sansevere-Dreher'],'Macmillan','1992-10-15',"Examines the adventures of such early explorers of America as Columbus, Dias, and Cabot. Includes information on the events, society, and superstitions of the times.",'0812520386',144,['Juvenile Nonfiction'],'http://books.google.com/books/content?id=3Gd5AG3Tp1wC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api',
        'http://books.google.com/books?id=3Gd5AG3Tp1wC&pg=PA140&dq=GOT&hl=&cd=7&source=gbs_api',False,'9.6 ounces'),
        Book('Got Your Back','Protecting Tupac in the World of Gangsta Rap',['Frank Alexander', 'Heidi Siegmund Cuda'],'Macmillan','2000-01-10',"An insider in the world of gangsta rap reveals his experiences, and the dark and violent underbelly of the music world that ultimately killed his charge, Tupac Shakur.",'0312242999',240,['Biography & Autobiography'],'http://books.google.com/books/content?id=_rTHNBvVBXwC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api',
        'http://books.google.com/books?id=_rTHNBvVBXwC&pg=PA198&dq=GOT&hl=&cd=9&source=gbs_api',False,'7.2 ounces'),
        Book('How We Got the Bible','',['Rose Publishing'],'Rose Publishing Inc','1998-04-01','Increase Your Confidence in the Reliability of the Bible How We Got the Bible will inspire your students with the stories of early Bible translators. This time line of key people and events in the history of the Bible shows ancient writing materials, such as stone and clay tablets, leather scrolls, papyrus, early hand copied books, and more. Features people who gave their lives to translating and printing the Bible, including William Tyndale, John Wycliffe, King James, Erasmus, and Johann Gutenberg. Size 8.5" x 5.5". Fits in a Bible cover. Unfolds to 33" long. Also available as a laminated or unlaminated wall chart, and a 10 pk of pamphlets, and a PowerPoint presentation.','9780965508261',12,['Bible'],'http://books.google.com/books/content?id=YboYSzVkUiAC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api',
        'http://books.google.com/books?id=YboYSzVkUiAC&pg=PP2&dq=GOT&hl=&cd=10&source=gbs_api',True,'1.6 ounces')
        ]),

        ("fdshjoaowl", None),

        ("", "LA SOLICITUD NO SE EJECUTÓ DE MANERA CORRECTA"))

        for entrada, salida in salida_esperadas:
            # comparaciones de la salida real con la esperada
            salida_real = APIConnection().getBook(entrada, APIServiceExtra())
            self.assertEqual(salida, salida_real)

if __name__ == "__main__":
    unittest.main()
