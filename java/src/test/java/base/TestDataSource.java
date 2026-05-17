package base;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class TestDataSource {
    private static JsonNode _testData;
    public static JsonNode testData() {
       if (_testData != null) return _testData;
       Path path = Paths.get("..", "test_data.json");
       File file = path.toFile();
        try {
            _testData = new ObjectMapper().readTree(file);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return _testData;
    }
}
