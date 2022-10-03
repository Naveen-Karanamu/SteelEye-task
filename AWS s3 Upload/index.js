// Libraries
import express from "express";
import AWS from "aws-sdk";
import multer from "multer";

const Router = express();

// Multer config
const storage = multer.memoryStorage();
const upload = multer({ storage });


// AWS s3 bucker config
const s3Bucket = new AWS.S3({
    accessKeyId: process.env.AWS_ACCESS_KEY_ID ,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
    region: "ap-south-1"
});

//function to Upload to s3
export const s3Upload = (options) => {
    return new Promise((resolve, reject) => {
        s3Bucket.upload(options, (error, data) => {
            if (error) return reject(error);
            return resolve(data);
        })
    })
}

/*
Route: /
Description: Upload given file to s3 bucket
params: NONE
Access: Public
Method: POST
*/
Router.post("/file/up", upload.single("file"), async (req, res) => {
    try {
        const file = req.file;

        // s3 Bucket options
        const bucketOptions = {
            Bucket: "steeleye-csv",
            Key: file.originalname,
            Body: file.buffer,
            ContentType: file.mimetype,
            ACL: "public-read"
        }

        // upload to s3 and returns the url of the file
        const uploadFile = await s3Upload(bucketOptions);

        return res.status(200).json({ uploadFile });
    } catch (error) {
        return res.status(500).json({ error: error.message });
    }
})

Router.get("/", (req, res) => res.json({ message: "Setup done" }));

Router.listen(3001, () => console.log("Server is Runnig 🚀"))

export default Router;