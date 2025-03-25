import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try {
            String apiKey = "67d940ed01f1642b7cd0d879";
            String query = "Powershell";
            int results = 10;
            String country = "us";
            int page = 0;
            String advance_search = "false";

            String apiUrl = "https://api.scrapingdog.com/google/?api_key=" + apiKey
                    + "&query=" + query
                    + "&results=" + results
                    + "&country=" + country
                    + "&page=" + page
                    + "&advance_search=" + advance_search;

            URL url = new URL(apiUrl);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");

            int responseCode = connection.getResponseCode();

            if (responseCode == 200) {
                BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
                String inputLine;
                StringBuilder response = new StringBuilder();

                while ((inputLine = reader.readLine()) != null) {
                    response.append(inputLine);
                }
                reader.close();

                System.out.println(response.toString());
            } else {
                System.out.println("HTTP request failed with response code: " + responseCode);
            }

            connection.disconnect();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
