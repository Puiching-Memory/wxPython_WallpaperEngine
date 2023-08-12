precision mediump float;

uniform float time;
uniform vec2 resolution;

float random (vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898,78.233))) * 43758.5453123);
}

void main() {
    vec2 st = gl_FragCoord.xy / resolution.xy;

    // Use the fragment position to create a random seed
    vec2 seed = vec2(floor(gl_FragCoord.x), floor(gl_FragCoord.y));

    // Get a random value for this fragment
    float noise = random(seed);

    // Map the noise value to a grayscale color
    vec3 color = vec3(noise);

    // Output the color of this fragment
    gl_FragColor = vec4(color, 1.0);
}
