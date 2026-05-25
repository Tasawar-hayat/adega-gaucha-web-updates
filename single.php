<?php
/**
 * The Template for displaying all single posts.
 * Upload this to your active theme folder to apply this design to ALL past and future blog posts.
 */
get_header(); 
?>

<!-- 100% GUARANTEED CSS INJECTION -->
<style>
    /* CSS Variables - Structural & Theme */
    :root {
        --ag-radius-md: 8px;
        --ag-radius-lg: 12px;
        --ag-accent: #F68625;
        
        /* Strict Color Rules */
        --ag-bg-main: #ffffff;
        --ag-text-main: #000000;
        --ag-border-accent: #F68625;
    }

    /* Base Layout */
    .ag-blog-container { 
        max-width: 1200px; 
        margin: 0 auto; 
        padding: 0 15px; 
        width: 100%; 
        box-sizing: border-box; 
        overflow-x: hidden;
        background-color: var(--ag-bg-main);
        color: var(--ag-text-main);
        animation: ag-fade-in 0.6s ease-out forwards;
    }
    
    @keyframes ag-fade-in {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .ag-blog-layout { 
        display: grid; 
        grid-template-columns: 1fr; 
        gap: 2rem; 
        padding: 2rem 0; 
        margin-top: 120px; 
        box-sizing: border-box; 
    }
    
    @media (min-width: 992px) { 
        .ag-blog-layout { 
            /* Content Left, Sidebar Right */
            grid-template-columns: 7fr 3fr; 
            gap: 4rem; 
            align-items: start; 
            margin-top: 150px; 
            padding: 3rem 0; 
        }
    }
    
    .ag-post-header { margin-bottom: 2rem; }
    
    /* Main Content Typography */
    .ag-post-title { 
        font-size: clamp(1.75rem, 5vw, 3rem); 
        line-height: 1.2; 
        margin-bottom: 1.5rem; 
        word-break: break-word; 
        color: var(--ag-text-main); 
        font-weight: 700;
    }
    
    .ag-post-featured-image-placeholder { 
        width: 100%; 
        border-radius: var(--ag-radius-lg); 
        margin-bottom: 1.5rem; 
        display: flex; 
        align-items: center; 
        justify-content: center; 
        overflow: hidden; 
    }
    
    .ag-post-featured-image-placeholder img { 
        width: 100%; 
        height: auto; 
        max-height: 600px; 
        object-fit: cover; 
        border-radius: var(--ag-radius-lg); 
    }
    
    /* META STYLING */
    .ag-post-meta { 
        display: flex; 
        justify-content: space-between; 
        align-items: center; 
        padding: 1.5rem 0; 
        border-top: 1px solid var(--ag-border-accent); 
        border-bottom: 1px solid var(--ag-border-accent); 
        margin-bottom: 2.5rem; 
        font-size: 0.95rem; 
        color: var(--ag-text-main); 
    }
    
    .ag-meta-left { display: flex; align-items: center; gap: 2rem; flex-wrap: wrap; }
    .ag-meta-time { display: flex; align-items: center; gap: 0.5rem; }
    .ag-meta-time svg { width: 18px; height: 18px; opacity: 0.8; }
    
    .ag-post-author { display: flex; align-items: center; gap: 0.75rem; }
    .ag-author-avatar-small { width: 32px; height: 32px; border-radius: 50%; overflow: hidden; background-color: #eee; }
    .ag-author-avatar-small img { width: 100%; height: 100%; object-fit: cover; }
    
    /* Share Buttons */
    .ag-post-share { display: flex; align-items: center; gap: 0.75rem; color: var(--ag-text-main); font-weight: 600; }
    .ag-share-btn { 
        width: 36px; 
        height: 36px; 
        border-radius: 50%; 
        background-color: var(--ag-bg-main); 
        border: 1px solid var(--ag-border-accent); 
        color: var(--ag-text-main); 
        display: flex; 
        align-items: center; 
        justify-content: center; 
        text-decoration: none; 
        transition: color 0.3s ease, border-color 0.3s ease; 
    }
    .ag-share-btn svg { width: 16px; height: 16px; fill: currentColor; }
    
    /* Strict Hover: BG stays white, border stays orange, text/icon turns orange */
    .ag-share-btn:hover { 
        color: var(--ag-accent); 
        background-color: var(--ag-bg-main); 
    }
    
    @media (max-width: 650px) {
        .ag-post-meta { flex-direction: column; align-items: flex-start; gap: 1.5rem; }
        .ag-meta-left { flex-direction: column; align-items: flex-start; gap: 1rem; }
    }
    
    /* Content Formatting */
    .ag-post-content { 
        font-size: 1.125rem; 
        line-height: 1.8; 
        width: 100%; 
        overflow-wrap: break-word; 
        word-wrap: break-word; 
        color: var(--ag-text-main); 
    }
    .ag-post-content h1, .ag-post-content h2, .ag-post-content h3, .ag-post-content h4, .ag-post-content h5, .ag-post-content h6 { 
        color: var(--ag-text-main); 
    }
    .ag-post-content h2 { font-size: 2rem; font-weight: 700; margin: 2.5rem 0 1rem; }
    .ag-post-content h3 { font-size: 1.5rem; margin: 2rem 0 1rem; }
    .ag-post-content p { margin-bottom: 1.5rem; }
    .ag-post-content blockquote { 
        font-size: 1.5rem; 
        font-style: italic; 
        border-left: 4px solid var(--ag-border-accent); 
        margin: 3rem 0; 
        padding: 1rem 1.5rem; 
        background: var(--ag-bg-main);
        color: var(--ag-text-main);
    }
    .ag-post-content img { max-width: 100%; height: auto; border-radius: var(--ag-radius-md); margin: 2rem 0; }
    .ag-post-content iframe { max-width: 100%; margin: 2rem 0; }
    
    /* SIDEBAR WIDGETS */
    .ag-sidebar { display: flex; flex-direction: column; gap: 2rem; width: 100%; }
    .ag-widget { 
        background-color: var(--ag-bg-main); 
        border: 1px solid var(--ag-border-accent); 
        border-radius: var(--ag-radius-md); 
        padding: 1.5rem; 
        box-sizing: border-box; 
        color: var(--ag-text-main); 
    }
    
    @media (min-width: 992px) { 
        .ag-sidebar-inner { position: sticky; top: 150px; display: flex; flex-direction: column; gap: 2rem; } 
    }
    
    .ag-widget-title { 
        font-size: 1.25rem; 
        font-weight: 700; 
        margin-bottom: 1.5rem; 
        padding-bottom: 0.75rem; 
        border-bottom: 2px solid var(--ag-border-accent); 
        color: var(--ag-text-main); 
    }
    .ag-more-posts-list { display: flex; flex-direction: column; gap: 1rem; }
    
    /* Sidebar Recent Posts Card */
    .ag-more-post-card { 
        display: flex; 
        gap: 1rem; 
        align-items: center; 
        padding-bottom: 1rem; 
        border-bottom: 1px solid var(--ag-border-accent); 
        text-decoration: none; 
        color: inherit; 
        transition: transform 0.3s ease; 
        background-color: var(--ag-bg-main);
    }
    .ag-more-post-card:last-child { border-bottom: none; padding-bottom: 0; }
    
    /* Hover Effect for Sidebar Cards: Only Title turns Orange */
    .ag-more-post-card:hover { transform: translateY(-2px); }
    .ag-more-post-card:hover .ag-more-post-title { color: var(--ag-accent); }
    
    .ag-more-post-thumb { width: 80px; height: 60px; border-radius: 4px; background-color: #eee; object-fit: cover; flex-shrink: 0; border: 1px solid var(--ag-border-accent); }
    .ag-more-post-title { 
        font-size: 0.95rem; 
        font-weight: 700; 
        line-height: 1.4; 
        margin: 0; 
        color: var(--ag-text-main); 
        transition: color 0.3s ease; 
    }
    
    /* Sidebar Contact Widget */
    .ag-contact-widget { text-align: center; }
    .ag-contact-btn { 
        display: inline-block; 
        padding: 0.75rem 1.5rem; 
        border-radius: var(--ag-radius-md); 
        font-weight: 700; 
        width: 100%; 
        border: 2px solid var(--ag-border-accent); 
        background-color: var(--ag-bg-main); 
        color: var(--ag-text-main); 
        text-align: center; 
        text-decoration: none; 
        box-sizing: border-box; 
        transition: color 0.3s ease, border-color 0.3s ease; 
    }
    /* Strict Hover for Button: Text turns Orange, background stays white */
    .ag-contact-btn:hover { 
        color: var(--ag-accent);
        border-color: var(--ag-accent);
    }
    
</style>

<main class="ag-blog-container ag-blog-layout">
    
    <?php 
    // START THE LOOP - Crucial for exposing all internal data properly
    while ( have_posts() ) : the_post(); 
    ?>

    <!-- Right Column (Main Content on Desktop, Top on Mobile) -->
    <article class="ag-main-column">
        
        <header class="ag-post-header">
            <!-- DYNAMIC POST TITLE -->
            <h1 class="ag-post-title"><?php the_title(); ?></h1>
            
            <!-- DYNAMIC FEATURED IMAGE -->
            <?php if (has_post_thumbnail()) : ?>
                <div class="ag-post-featured-image-placeholder">
                    <?php the_post_thumbnail('large'); ?>
                </div>
            <?php endif; ?>
            
            <!-- DYNAMIC META DATA -->
            <div class="ag-post-meta">
                <div class="ag-meta-left">
                    <?php 
                        $content = get_the_content();
                        $word_count = str_word_count(strip_tags($content));
                        $reading_time = ceil($word_count / 200);
                        if ($reading_time == 0) { $reading_time = 1; }
                    ?>
                    <span class="ag-meta-time">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                        <?php echo $reading_time; ?> min read
                    </span>
                    
                    <div class="ag-post-author">
                        <div class="ag-author-avatar-small"><?php echo get_avatar(get_the_author_meta('ID'), 32); ?></div>
                        <span><?php the_author(); ?></span>
                    </div>
                </div>
                
                <div class="ag-post-share">
                    <span>Share:</span>
                    <a href="https://www.facebook.com/sharer/sharer.php?u=<?php echo urlencode(get_permalink()); ?>" target="_blank" class="ag-share-btn" title="Share on Facebook">
                        <svg viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
                    </a>
                    <a href="https://twitter.com/intent/tweet?url=<?php echo urlencode(get_permalink()); ?>&text=<?php echo urlencode(get_the_title()); ?>" target="_blank" class="ag-share-btn" title="Share on X">
                        <svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg>
                    </a>
                    <a href="https://www.linkedin.com/shareArticle?mini=true&url=<?php echo urlencode(get_permalink()); ?>&title=<?php echo urlencode(get_the_title()); ?>" target="_blank" class="ag-share-btn" title="Share on LinkedIn">
                        <svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                    </a>
                </div>
            </div>
        </header>

        <!-- DYNAMIC MAIN CONTENT - Nothing is hidden! -->
        <div class="ag-post-content">
            <?php the_content(); ?>
        </div>

    </article>

    <!-- Sidebar -->
    <aside class="ag-sidebar">
        <div class="ag-sidebar-inner">
            
            <!-- DYNAMIC Recent Posts Widget -->
            <div class="ag-widget">
                <h3 class="ag-widget-title">Latest Posts</h3>
                <div class="ag-more-posts-list">
                    <?php
                    $recent_posts = new WP_Query(array(
                        'posts_per_page' => 3,
                        'post_status' => 'publish',
                        'post__not_in' => array(get_the_ID())
                    ));
                    if ($recent_posts->have_posts()) :
                        while ($recent_posts->have_posts()) : $recent_posts->the_post();
                    ?>
                        <a href="<?php the_permalink(); ?>" class="ag-more-post-card">
                            <?php if (has_post_thumbnail()) : ?>
                                <?php the_post_thumbnail('thumbnail', ['class' => 'ag-more-post-thumb']); ?>
                            <?php else: ?>
                                <div class="ag-more-post-thumb"></div>
                            <?php endif; ?>
                            <h4 class="ag-more-post-title"><?php the_title(); ?></h4>
                        </a>
                    <?php 
                        endwhile;
                        wp_reset_postdata();
                    else:
                    ?>
                        <p>No recent posts found.</p>
                    <?php endif; ?>
                </div>
            </div>

            <!-- Contact/CTA Widget -->
            <div class="ag-widget ag-contact-widget">
                <h3 class="ag-widget-title">Join Us</h3>
                <p>Experience the authentic taste of Southern Brazil.</p>
                <a href="/reservations" class="ag-contact-btn">Reserve Your Table</a>
            </div>

        </div>
    </aside>

    <?php endwhile; // End of the WordPress loop ?>

</main>

<?php get_footer(); ?>
