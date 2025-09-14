import http from 'k6/http';

export const options = {
    // stages: [
    //     { duration: '20s', target: 50 , timeout: 1000},
    // ],
};

export default function () {
    const url = 'http://localhost:8081/';
    http.get(url);
}
