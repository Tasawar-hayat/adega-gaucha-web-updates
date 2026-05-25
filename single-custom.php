<?php
/**
 * Template Name: Custom Blog Post Template
 * Template Post Type: post
 * 
 * Instructions: 
 * If you want to use this PHP template, upload it to your active WordPress theme folder 
 * (e.g., wp-content/themes/your-theme/single.php). It will automatically pull the dynamic 
 * data (Title, Content, Images) from your WordPress posts.
 */
get_header(); 
?>

<!-- Ensure you enqueue or link your style.css here -->
<main class="container blog-layout">
    
    <!-- Left Column: Content -->
    <article class="main-column">
        
        <header class="post-header">
            <!-- DYNAMIC POST TITLE -->
            <h1 class="post-title"><?php the_title(); ?></h1>
            
            <!-- DYNAMIC FEATURED IMAGE -->
            <?php if (has_post_thumbnail()) : ?>
                <div class="post-featured-image-placeholder" style="background:transparent;">
                    <?php the_post_thumbnail('large', ['style' => 'width:100%; height:auto; border-radius:12px; object-fit:cover; aspect-ratio:16/9;']); ?>
                </div>
            <?php endif; ?>
            
            <!-- DYNAMIC META DATA -->
            <div class="post-meta">
                <div class="post-author">
                    <div class="author-avatar"><?php echo get_avatar(get_the_author_meta('ID'), 40); ?></div>
                    <span><?php the_author(); ?></span>
                </div>
                <div class="post-share">
                    <span style="opacity:0.8; font-size:0.85rem; text-transform:uppercase; letter-spacing:1px; font-weight:600;">Share:</span>
                    <!-- DYNAMIC SHARE LINKS -->
                    <a href="https://www.facebook.com/sharer/sharer.php?u=<?php echo urlencode(get_permalink()); ?>" target="_blank" class="share-icon" title="Share on Facebook">
                        <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
                    </a>
                    <a href="https://twitter.com/intent/tweet?url=<?php echo urlencode(get_permalink()); ?>&text=<?php echo urlencode(get_the_title()); ?>" target="_blank" class="share-icon" title="Share on X">
                        <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg>
                    </a>
                    <a href="https://www.linkedin.com/shareArticle?mini=true&url=<?php echo urlencode(get_permalink()); ?>&title=<?php echo urlencode(get_the_title()); ?>" target="_blank" class="share-icon" title="Share on LinkedIn">
                        <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                    </a>
                </div>
            </div>
        </header>

        <!-- DYNAMIC MAIN CONTENT -->
        <div class="post-content">
            <?php the_content(); ?>
        </div>

    </article>

    <!-- Right Column (Sidebar) -->
    <aside class="sidebar">
        <div class="sidebar-inner">
            
            <!-- DYNAMIC Recent Posts Widget -->
            <div class="widget">
                <h3 class="widget-title">Latest Posts</h3>
                <div class="more-posts-list">
                    <?php
                    $recent_posts = new WP_Query(array(
                        'posts_per_page' => 3,
                        'post_status' => 'publish',
                        'post__not_in' => array(get_the_ID())
                    ));
                    if ($recent_posts->have_posts()) :
                        while ($recent_posts->have_posts()) : $recent_posts->the_post();
                    ?>
                        <a href="<?php the_permalink(); ?>" class="more-post-card">
                            <?php if (has_post_thumbnail()) : ?>
                                <?php the_post_thumbnail('thumbnail', ['class' => 'more-post-thumb']); ?>
                            <?php else: ?>
                                <div class="more-post-thumb"></div>
                            <?php endif; ?>
                            <h4 class="more-post-title"><?php the_title(); ?></h4>
                        </a>
                    <?php 
                        endwhile;
                        wp_reset_postdata();
                    endif; 
                    ?>
                </div>
            </div>

            <!-- Contact/CTA Widget (Static) -->
            <div class="widget contact-widget">
                <h3 class="widget-title">Join Us</h3>
                <p>Experience the authentic taste of Southern Brazil.</p>
                <a href="/reservations" class="contact-btn">Reserve Your Table</a>
            </div>

        </div>
    </aside>
</main>

<!-- Bottom Section: DYNAMIC Discover More -->
<section class="discover-section">
    <div class="container">
        <h2 class="section-title">Discover More</h2>
        <div class="grid-3">
            <?php
            $related_posts = new WP_Query(array(
                'posts_per_page' => 3,
                'orderby' => 'rand',
                'post__not_in' => array(get_the_ID())
            ));
            if ($related_posts->have_posts()) :
                while ($related_posts->have_posts()) : $related_posts->the_post();
            ?>
                <article class="post-card">
                    <?php if (has_post_thumbnail()) : ?>
                        <?php the_post_thumbnail('medium', ['class' => 'card-img']); ?>
                    <?php else: ?>
                        <div class="card-img"></div>
                    <?php endif; ?>
                    <div class="card-content">
                        <h3 class="card-title"><?php the_title(); ?></h3>
                        <div class="post-author" style="margin-bottom:1rem;">
                            <div class="author-avatar" style="width:24px;height:24px;"><?php echo get_avatar(get_the_author_meta('ID'), 24); ?></div>
                            <span style="font-size:0.875rem;"><?php the_author(); ?></span>
                        </div>
                        <a href="<?php the_permalink(); ?>" class="read-more">Read More &raquo;</a>
                    </div>
                </article>
            <?php 
                endwhile;
                wp_reset_postdata();
            endif; 
            ?>
        </div>
    </div>
</section>

<?php get_footer(); ?>
