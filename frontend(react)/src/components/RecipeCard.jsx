// PromptCard component receives post data and callback functions as props
const PromptCard = ({ post, handleTagClick, handleEdit, handleDelete }) => {
  // Get user session data using the useSession hook
  const { data: session } = useSession();
  // Get the current pathname and router object using Next.js navigation hooks
  const pathName = usePathname();
  const router = useRouter();

  // State to manage the copied status of the prompt
  const [copied, setCopied] = useState("");

  // Function to handle copying the prompt text to the clipboard
  const handleCopy = () => {
    setCopied(post.prompt);
    navigator.clipboard.writeText(post.prompt);
    // Reset the copied status after 3 seconds
    setTimeout(() => setCopied(""), 3000);
  };

  // Render the PromptCard component
  return (
    <div className="prompt_card">
      <div className="flex justify-between items-start gap-5">
        <div className="flext-1 flex justify-start items-center gap-3 cursor-pointer">
          <Image
            src={post.creator.image}
            alt="user_image"
            width={40}
            height={40}
            className="rounded-full object-contain"
          />
          <div className="flex flex-col">
            <h3 className="font-satoshi font-semibold text-gray-900 ">
              {post.creator.username}
            </h3>
            <p className="font-inter text-sm text-gray-500">
              {post.creator.email}
            </p>
          </div>
        </div>
      </div>
      <p className="my-4 font-satoshi text-sm text-gray-700">{post.prompt}</p>

        <div className="mt-5 flex-center gap-4 border-t border-gray-100 pt-3">
          <p
            className="font-inter text-sm green_gradient cursor-pointer"
            onClick={handleEdit}
          >
            Edit
          </p>
          <p
            className="font-inter text-sm orange_gradient cursor-pointer"
            onClick={handleDelete}
          >
            Delete
          </p>
        </div>
    
    </div>
  );
};

export default PromptCard;
