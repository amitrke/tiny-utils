// List files from AWS Multi Region Access Point

Class MrapConnect {
    public static void main(String[] args) {
        System.out.println("Hello, World!");

        // Create an S3 client
        Region region = Region.US_EAST_1;
        S3Client s3 = S3Client.builder()
                .region(region)
                .build();
        mrap = "arn:aws:s3::123456789012:accesspoint/myendpoint";
        ListObjectsRequest listObjects = ListObjectsRequest
                .builder()
                .bucket(mrap)
                .build();
        ListObjectsResponse res = s3.listObjects(listObjects);
        for (S3Object content : res.contents()) {
            System.out.println(content.key());
        }
    }
}