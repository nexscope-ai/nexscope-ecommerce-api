import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.Duration;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Run {
    private static String field(String json, String name) {
        Matcher matcher = Pattern.compile("\\\"" + Pattern.quote(name) + "\\\"\\s*:\\s*\\\"((?:\\\\.|[^\\\"])*)\\\"").matcher(json);
        if (!matcher.find()) throw new IllegalArgumentException("Missing " + name);
        return matcher.group(1).replace("\\/", "/");
    }

    public static void main(String[] args) throws Exception {
        if (args.length == 0) throw new IllegalArgumentException("Pass an example directory inside demos/");
        Path folder = Path.of(args[0]).toAbsolutePath().normalize();
        Path root = Path.of("").toAbsolutePath().normalize();
        if (!folder.startsWith(root.resolve("demos"))) throw new IllegalArgumentException("Example must be inside demos/");
        String config = Files.readString(folder.resolve("example.json"), StandardCharsets.UTF_8);
        Path payloadPath = root.resolve(field(config, "payload")).normalize();
        if (!payloadPath.startsWith(root)) throw new IllegalArgumentException("Payload must be inside repository");
        String request = Files.readString(payloadPath, StandardCharsets.UTF_8).trim();
        String endpoint = field(config, "endpoint");
        String payload = field(config, "mode").equals("mcp")
                ? "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/call\",\"params\":{\"name\":\"" + field(config, "mcpToolName") + "\",\"arguments\":" + request + "}}"
                : request;
        System.out.println("POST " + endpoint);
        System.out.println(payload);
        if (args.length < 2 || !args[1].equals("--execute")) {
            System.out.println("Preview only. Add --execute to send.");
            return;
        }
        if (Pattern.compile("https?://(?:[^\\s\\\"]*\\.)?(?:example\\.com|example\\.org|example\\.net)", Pattern.CASE_INSENSITIVE).matcher(request).find()) {
            throw new IllegalArgumentException("Replace example.com/example.org/example.net URLs before executing");
        }
        String key = System.getenv("NEXSCOPE_API_KEY");
        if (key == null || key.isBlank()) throw new IllegalArgumentException("NEXSCOPE_API_KEY is required");
        HttpRequest httpRequest = HttpRequest.newBuilder(URI.create(endpoint))
                .timeout(Duration.ofSeconds(120))
                .header("Authorization", "Bearer " + key)
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8))
                .build();
        HttpResponse<String> response = HttpClient.newHttpClient().send(httpRequest, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
        if (response.statusCode() >= 400) throw new IllegalStateException("HTTP " + response.statusCode());
        if (Pattern.compile("\\\"code\\\"\\s*:\\s*(?!0\\b)-?\\d+").matcher(response.body()).find()
                || Pattern.compile("\\\"error\\\"\\s*:\\s*\\{").matcher(response.body()).find()
                || Pattern.compile("\\\"isError\\\"\\s*:\\s*true").matcher(response.body()).find()) {
            throw new IllegalStateException("API returned an error");
        }
    }
}
