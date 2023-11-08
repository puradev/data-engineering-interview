from requests import Response, Session, exceptions as re
import json
import os

endpoint_url = os.environ["RANDO_API_URL"]
class RandomUserLoader():
    def _get_users_json(self, url:str)->list[dict]:
        new_session = Session()
        try:
            response = new_session.get(url=url)
        except re.HTTPError as e:
            return "Encountered Error Response From Server: " + str(e)
        response = response.json()
        return response["results"]

    def _parse_user_json(self,user:dict)->dict:

        user_dict = {
            "first_name":user.get("name","N/A").get("first", "N/A"),
            "last_name":user.get("name","N/A").get("last", "N/A"),
            "gender":user.get("gender", "N/A"),
            "email_address":user.get("email", "N/A"),
            "date_of_birth":user.get("dob","N/A").get("date", "N/A"),
            "phone_number":user.get("phone", user.get("cell", "N/A")),
            "nationality":user.get("nat", "N/A")
        }

        return user_dict
    
    def _write_user_results_file(self, url):
        users = self._get_users_json(url=url)
        
        with open("./user_information.json","w",encoding='utf-8') as user_file:
            for user in users:
                user_dict = self._parse_user_json(user)
                user_json = json.dumps(user_dict,ensure_ascii=False)
                user_file.write(user_json + '\n')
            
        

if __name__=="__main__":
    loader = RandomUserLoader()
    loader._write_user_results_file(url = endpoint_url)
        